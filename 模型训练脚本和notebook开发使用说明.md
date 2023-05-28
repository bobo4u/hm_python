## 模型训练脚本和notebook开发使用说明

### 1.notebook开发简要教程

​	此教程以语义分割LinkNet34网络结构，Pytroch框架，数据集GID-RGB-15classes 为示例

​	创建notebook

![1622716537_1_.png](https://i.loli.net/2021/06/03/9hjsPiQwqZY3bRx.png)

```text
### 训练步骤
1. input()获取训练参数，参数详情可查看3.1
2. 加载预训练模型,从s3上获取（可选），使用aiUtils工具包
3. 获取s3上数据，使用aiUtils工具包
4. 训练集训练
5. 验证集训练
6. 中间输出
    -  训练日志，记录epoch评价指标，输出trainlog.json样式
    -  图片输出，每个epoch输出一次图片
    -  权重文件
```

#### 1.1 导入包

如果导入aiUtils报错，请参考2.1依赖库安装

``` python
# 导入网络结构，LinkNet34为例
from linknet34 import LinkNet34
# 导入读取s3数据工具包
from aiUtils import aiUtils
# 导入其他工具包
import os
import json
import io
from PIL import Image
import numpy as np

# 获取当前项目路径 
basedir = os.getcwd()
```
#### 1.2 获取参数

##### 1.2.1 加载输入参数流
![1622714207_1_.png](https://i.loli.net/2021/06/03/xeub1JDa5Rq9j27.png)

##### 1.2.2 获取数据
```python
# 获取参数后可进行数据处理(部分)
model_name = params["model_name"]
dataset_id = params["dataset_id"]
resume_path = params["resume_path"]
n_class =  int(params["n_class"])
batch_size =  int(params["batch_size"])
epochs =  int(params["epochs"])
training_id =  params["training_id"]
class_name =  params["class_name"]

# gpu
device_ids = []
gpu_num = int(params['gpu_num'])
if gpu_num == 0:
    gpu_ids = -1  # for CPU
else:
    for i in range(0, gpu_num):
        device_ids.append(i)
        
# 图片标签处理（中间图片输出类别颜色需与label颜色一致）
labels = params['label']
labels = eval(labels)
rgb_value = {}
acval_realval = {}

for i, val in enumerate(labels):
    for key in val.keys():
        if key == "class_color":
            color_ = val[key]
            rgb = tuple(list(map(int, color_.split(','))))
        elif key == "class_value":
            value = int(val[key])
            trainValue = int(i)
        else:
            continue
    if rgb and value >= 0:
        rgb_value[rgb] = value
        acval_realval[value] = trainValue
```

#### 1.2 加载预训练模型


##### 1.2.1 s3工具包aiUtils说明

- **连接 S3**:
    - notebook中 dataset_id为空，通过环境变量传值
    
- **工具包属性**：
    - path 对应数据s3的key,
    - 例如：s3://pie-engine-ai/devel/system/dataset/segmentation/92008494-0976-4ed5-bb65-e8b565e54dbd/

- **工具包方法**：
    - downS3Weight(s3WightKey,saveWightDir)  从S3上下载权重文件
    - getImages(path)  获取s3对应key下的所有数据列表
    - getImgXmlArray(dataPath)  获取s3指定数据的数据流

##### 1.2.2 加载预训练模型
```python
# 加载模型
model = LinkNet34(n_class)

# 连接s3
if dataset_id == "":
    dataset_id = None
s3Client = aiUtils.s3GetImg(datasetId=dataset_id)

# resume_path 预训练权重文件存放key，将预训练权重文件拉取到本地basedir中，进行加载
if resume_path:
    resume_path = "/".join(resume_path.split("/")[3:])
    print('Loading weights into state dict...')
    # 拉取预训练权重文件
    s3Client.downS3Weight(basedir + '/' + model_name + ".th",resume_path + model_name + ".th")
    # 模型加载权重文件
    model.load_state_dict(basedir + '/' + model_name + ".th")
```

#### 1.3 读取数据

##### 1.3.1 aiUtils工具包属性及方法示例展示

![1622714392_1_.png](https://i.loli.net/2021/06/03/U3BbW1r4iHvXASp.png)

![1622714420_1_.png](https://i.loli.net/2021/06/03/5Q4ORgHxIUJcL8j.png)

![1622714433_1_.png](https://i.loli.net/2021/06/03/3lCDFSPQK2ZBRf5.png)
##### 1.3.2 创建数据迭代器
- 训练集: datasets_path + "train/"
- 验证集: datasets_path + "valid/"
- ImageDataset 自定义获取数据，返回 image、label对应的数据，并可以进行数据处理
- path + "images" ：图片和标签文件夹名称与相应的类别相关，详情查看3.2

```python
# 自定义数据读取及数据
import torch.utils.data as data
class ImageDataset(data.Dataset):
    
    def __init__(self, path, s3Client):
        # 图片路径
        path = "/".join(path.split("/")[3:])
        self.images = s3Client.getImages(path + "images")
        
    def __getitem__(self, index):
        # 图片路径
        image_path = self.images[index]
        # 图片对应的标签路径
        label_path = image_path.replace('images', 'labels')
        # 目标识别则需要将后缀换为xml
        
        # 读取图片
        imgBody = s3Client.getImgXmlArray(image_path)
        pillowImage = Image.open(io.BytesIO(imgBody))
        img = np.asarray(pillowImage)
        
        # 读取标签
        labelBody = s3Client.getImgXmlArray(label_path)
        pillowLable = Image.open(io.BytesIO(labelBody))
        label = np.asarray(pillowLable)
        
        # 数据再处理
        # 数据增强
        
        return torch.Tensor(img),torch.Tensor(label)
    
    def __len__(self):
        return len(self.images)
        
```
##### 1.3.3 迭代器获取数据

```python
from torch.utils.data import DataLoader

# 自定义获取数据、数据预处理
# 训练集
train_dataset = ImageDataset(dataset_path + "train/",s3Client)
train_data_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=0)

# 验证集
valid_dataset = ImageDataset(dataset_path + "valid/",s3Client)
valid_data_loader = DataLoader(valid_dataset, batch_size=batch_size, shuffle=True, num_workers=0)
```

#### 1.4 训练数据并输出日志、图片、权重文件
##### 1.4.1 输出存放位置
```python
# 输出日志及图片、权重文件存放路径
outputSaveDir = basedir + '/output'
if not os.path.exists(outputSaveDir + '/picture/'):
    os.makedirs(outputSaveDir + '/picture/')

# 训练需输出的其他文件存放
if not os.path.exists(outputSaveDir + '/files/'):
    os.makedirs(outputSaveDir + '/files/')
```
##### 1.4.2 初始化json文件
```python
import time

start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
log = {'training_id': training_id,"create_time": start_time,"description":{"precision":"精确度","recall":"召回率","score":"F1分数"},
       "epochs": [], 'best': "", "end_time":""}
```

##### 1.4.3 批次进行训练，在epoch中输出图片，保存权重文件，保存日志
```python
import torch

for epoch in range(0, epochs):
    # 获取训练集数据
    train_data_loader_iter = iter(train_data_loader)
    # 获取验证集数据
    valid_data_loader_iter = iter(valid_data_loader)
    
    # 训练集进行训练
    for img, mask in train_data_loader_iter:
        # img mask训练集对应图片及标签
        train_img = img
        train_mask = mask
        # 训练
            # 定义学习率 optimizer
            # 训练网络结构 pred = model.forward(img)
            # 损失值计算 loss(pred,mask)
            # loss.backward()
            # 学习率变化 optimizer.step()
        # 计算训练评价指标 loss、precision、recall、score、iou等
        
     # 验证集进行训练
    for img, mask in valid_data_loader_iter:
        # img mask对应验证集图片及标签
        valid_img = img
        valid_mask = mask
        # 训练
            # 训练网络结构 pred = model.forward(img)
            # 损失值计算 loss(pred,mask)
        # 计算训练评价指标 loss、precision、recall、score、iou等
    
    # 保存权重文件 
    weightDir = outputSaveDir + model_name + '.th'
    torch.save(model.state_dict(), weightDir)
    
    # 输出中间图片,需要输出颜色与lable中相应类别一致
    save_image(img,mask,pred)
    
    
    # 记录日志
    train = []
    valid = []
    
    # 所有类别平均指标
    train.append({
            "class": "all",
            "values": {
                "precision": '训练平均精确度指标', 
                "recall": '训练平均召回率指标',
                "score": '训练平均召回率指标',
            }
        })
    valid.append({
            "class": "all",
            "values": {
                "precision": '验证平均精确度指标', 
                "recall": '验证平均召回率指标',
                "score": '验证平均召回率指标',
            }
        })
    # 记录每个类别评价指标
    class_name_array = class_name.split(',')
    for ii,name in enumerate(class_name_array):
        train.append({"class":name,"values":{"precision":'训练集对应类别精确度指标',"recall":'训练集对应类别召回率指标',
                                "score":'训练集对应类别得分指标'}})
        valid.append({"class":name,"values":{"precision":'验证集对应类别精确度指标',"recall":'验证集对应类别召回率指标',
                                "score":'验证集对应类别得分指标'}})
    
    # 加入log日志
    log["epochs"].append({"epoch": epoch+1, "train": train, "valid": valid})
    log["best"] = {"score": best_score, "precision": best_precision, "recall": best_recall}
    
    
    # 在最后批次时
    if epoch == epochs-1:
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log["end_time"] = end_time
            
    # 每批次保存trailog.json日志
    trainlog = json.dumps(log, indent=4)
    with open(outputSaveDir + '/trainlog.json', 'w', encoding='utf-8') as log_file:
        log_file.write(trainlog)
    
    # 每个批次完成后输出如下信息
    print("[Process: {process}]".format(process=str(epoch + 1) + '/' + str(epochs)))
```



### 2.Notebook环境下开发说明

#### 2.1 第三方依赖库安装

​	在notebook中编写代码，可能会出现缺少第三方依赖库的情况，需要用户手动使用pip命令进行安装，如下所示，以导入平台的云端数据访问接口aiUtils为例

​	点击Pytorch-1.2.0，进行pytorch环境的notebook

![image-20210603095441008.png](https://i.loli.net/2021/06/03/cJaNVGkL1Zf6TyS.png)

​	导入aiUtils接口，提示错误，缺少requests和boto3库，需要在notebook环境下进行安装

![image-20210603095620716.png](https://i.loli.net/2021/06/03/7n65jCGWT8dAuFH.png)

​	点击terminal进行终端，切换到pytorch环境，使用pip install进行安装

![image-20210603095746835.png](https://i.loli.net/2021/06/03/oYyBG7vD25NhIm1.png)

![image-20210603095900225.png](https://i.loli.net/2021/06/03/de5bX9rxwZYIC2a.png)

![image-20210603100136189.png](https://i.loli.net/2021/06/03/UnFcqulXEzP32jK.png)

​	再次执行from aiUtils import aiUtils成功

![image-20210603100303405.png](https://i.loli.net/2021/06/03/zFBeNi8kbI6owhA.png)



#### 2.2 脚本访问数据集

​	notebook在启动时可以选择挂载数据集，在notebook内部使用代码访问数据集，可以参考1.2中的代码，区别在于notebook中无需传入数据集ID参数，该参数已经写入到notebook的环境变量。具体代码可以参考如下所示：

```python
from aiUtils import aiUtils

'''初始化获取数据集的访问接口
获取数据集在S3上的路径
获取训练集样本原始影像的文件夹路径
获取样本原始影像的文件路径数组'''
dataset_interface = aiUtils.s3GetImg()

train_images_path = dataset_path + 'train/A'
train_images_path = "/".join(train_images_path.split("/")[3:])

img_files = dataset_interface.getImages(train_images_path)
print("Count of train image files:", len(img_files))
print("First train image file path:", img_files[0])
```

​	运行效果如下所示：

![image-20210603101239969.png](https://i.loli.net/2021/06/03/oAQ1jmhbpKH9V6P.png)




### 3.用于模型训练的网络结构脚本开发规范

​	**要求**：训练代码的入口脚本文件名称必须为**train.py**

#### 3.1 界面选择的参数信息读取

​	模型训练启动时，界面上选取的网络结构、数据集、训练超参数等信息将以json的形式传递给模型训练的python脚本，参数信息json示例如下所示：

```json
{
    "auto_termination":0,
    "batch_size":4,
    "class_name":"airplane",
    "dataset_id":"49779ee7-1d00-4884-bf9a-dbc0802651e3",
    "epochs":80,
    "gpu_num":1,
    "label":"[{\"class_name\":\"airplane\",\"class_value\":1,\"class_title\":\"飞机\",\"class_color\":\"255,0,0\"}]",
    "learning_rate":0.0003,
    "load_size":"608,608",
    "model_name":"yolov4",
    "n_class":"1",
    "resume_path":"",
    "training_id":"57fc8152-c4f5-44b5-a25d-bc043a624d4b"
}
```

参数信息说明：

- **training_id:**本次训练的平台内部ID号，由平台内部自动生成

- **resume_path**:预训练模型的路径，未选择时为空

![image-20210602100508009.png](https://i.loli.net/2021/06/03/hDlF6JCyQ3tvkru.png)

- **dataset_id**:训练使用的数据集ID号

- **class_name**:用于训练的样本类别，多类别用逗号隔开，对于语义分割和变化检测，默认会带上background（背景）类别，例如:**"class_name"："background,road"**

- **label**:训练选取的类别标签信息，"class_name"表示标签名称，"class_value"表示类别在标签上的像素值，”class_title“表示类别的标题，”class_color“表示类别在图像上显示的颜色；信息从数据集中获取，详见数据集上传中说明，例如：**"label"："[{\"class_number\":0,\"class_name\":\"background\",\"class_value\":0,\"class_title\":\"背景\",\"class_color\":\"0,0,0\"}，{\"class_number\":3251,\"class_name\":\"road\",\"class_value\":255,\"class_title\":\"道路\",\"class_color\":\"255,255,255\"}]"**

- **n_class**:训练选取的类别个数

- **load_size**:训练使用的样本图片大小

  ![image-20210602103025495.png](https://i.loli.net/2021/06/03/Ze7RA1tNuqPfi6Q.png)

- **model_name**:训练使用的网络结构名称
- **learning_rate**:学习率
- **epochs**:迭代次数
- **batch_size**:批次大小，GPU每次加载的样本图片数，显存越大可加载的图片数越多，图片越小可加载的图片数据越多

- **auto_termination**:精度不再提升时自动终止训练，取值为0或1，0表示未勾选，1表示勾选

![image-20210602100108641.png](https://i.loli.net/2021/06/03/eBpc4qS6NFjy8fH.png)

- **gpu_num**:训练使用的GPU数量

![image-20210602103738509.png](https://i.loli.net/2021/06/03/T2Itzm5JMBX8SGC.png)

​	界面参数读取的python代码示例：

```python
import argparse
import json
import numpy as np

if __name__ == '__main__':
    # 定义训练参数
    parser = argparse.ArgumentParser(description='Read training config parameter...')
    parser.add_argument('--training_id', default='', type=str, help='训练id')
    parser.add_argument('--resume_path', default='', type=str, help='预训练模型路径')
    
    parser.add_argument('--dataset_id', default='', type=str, help='数据集id')
    parser.add_argument('--dataset_path', default='', type=str, help='数据集S3的访问地址')
    parser.add_argument('--class_name', default='', type=str, help='选定的样本类别')
    parser.add_argument('--label', default='', type=str, help='样本类别的标签信息')
    parser.add_argument('--n_class', default='', type=str, help='选定样本类别的数目，不包括background')
    parser.add_argument('--load_size', default='', type=str, help='选择样本的图片大小')
    
    parser.add_argument('--model_name', default='', type=str, help='网络结构名称')
    parser.add_argument('--learning_rate', default=0.0, type=float, help='学习率')
    parser.add_argument('--epochs', default=0, type=int, help='迭代次数')
    parser.add_argument('--batch_size', default=0, type=int, help='批次大小')
    parser.add_argument('--auto_termination', default=0, type=int, help='精度不再提升是否终止')
    
    parser.add_argument('--gpu_num', default=1, type=int, help='训练使用的GPU数量')
    
    args = parser.parse_args()
    print("start get training parameter...")
    
    # 读取传入的json训练参数
    #conf = input()
    #params = json.loads(conf)
    config_path = "traincfg.json"
    with open(config_path, 'r', encoding='utf-8') as f:
        params = json.load(f)
    
    args.training_id = str(params['training_id'])
    args.resume_path = params['resume_path']
    
    args.dataset_id = params['dataset_id']
    args.class_name = params["class_name"]
    args.class_name = args.class_name.replace('background,','')
    
    # 解析样本类别的标签颜色，并进行序列对应
    # 标签颜色对应相应的数据值
    args.rgb_value = {}
    # 标签值对应训练序号值
    args.val_acVal = {}
    labels = params['label']
    labels = eval(labels)
    for i,val in enumerate(labels):
        for key in val.keys():
            if key == "class_color":
                color_ = val[key]
                color_tuple = tuple(np.array(color_.split(',')).astype(int))
            elif key == "class_value":
                value = int(val[key])
                trainValue = int(i)
            else:
                continue
        if color_tuple and value >= 0:
            args.rgb_value[rgb] = value
            args.val_acVal[value] = trainValue
    
    args.n_class = int(params["n_class"])
    # 针对yolov4网络结构的特殊处理，yolov4的输入大小必须是32的整数倍
    args.load_size = params['load_size'].split(',')
    args.load_size[0] = round(float(args.load_size[0])/32) * 32
    args.load_size[1] = round(float(args.load_size[1])/32) * 32
    
    args.model_name = params["model_name"]
    args.learning_rate = float(params['learning_rate'])
    args.epochs = int(params['epochs'])
    args.batch_size = int(params['batch_size'])
    args.auto_termination = int(params["auto_termination"])
								  
    device_ids = []
    args.gpu_num = int(params['gpu_num'])
    if args.gpu_num != 0:
        for i in range(0, args.gpu_num):
            device_ids.append(i)
    
    args.device_ids = device_ids
```



#### 3.2 训练脚本访问数据集

- **初始化接口**

​	平台内置了aiUtils接口用于访问数据集，初始化数据集访问接口代码如下所示：

```python
# 导入aiUtils接口
from aiUtils import aiUtils

# 初始化获取数据集的访问接口
dataset_interface = aiUtils.s3GetImg(args.dataset_id)
```

- **数据集样本文件访问**

**（1）目录结构**

​	**目标识别**样本文件目录组织结构如下所示：

![image-20210602134811523.png](https://i.loli.net/2021/06/03/jafkOJUS3ADZdPI.png)

​	数据集分为训练集和验证集两个部分，影像存放在images文件夹下，样本标签存放在labels文件夹下，目标识别的标签文件采用VOC格式的XML进行存储，且文件名与images文件夹下的影像一一对应。

​	**语义分割**样本文件目录组织结构如下所示：

![image-20210602164631462.png](https://i.loli.net/2021/06/03/FYtL6TWbmPwCXNa.png)

​		和目标识别类似，数据集分为训练集和验证集两个部分，影像存放在images文件夹下，样本标签存放在labels文件夹下，原始影像和标签文件均为图片格式，且文件名一一对应。

​	**变化检测**样本文件目录组织结构如下所示：

![image-20210602165759310.png](https://i.loli.net/2021/06/03/1HOCw6qUX7nQdNW.png)

​	数据集中的训练集样本放在train文件夹下，验证集样本放在valid文件夹下，A表示变化前的样本图像，B表示变化后的样本图像，labels为变化标签图像，且A、B、labels中的文件名一一对应。

**（2）读取图片**

​	首先获取到dataset_id对应数据的存储路径，根据目录结构确定获取影像的路径，利用getImgXMLArray()方法读取图像的二进制流，具体代码如下：

```python
# 获取数据集在S3上的路径
dataset_path = dataset_interface.path

# 获取训练集样本原始影像的文件夹路径
train_images_path = dataset_path + 'train/images'
train_images_path = "/".join(train_images_path.split("/")[3:])
# 获取样本原始影像的文件路径数组
img_files = dataset_interface.getImages(train_img_path)
print("Count of train image files:", len(img_files))
print("First train image file path:", img_files[0])

from PIL import Image
import io

# 读取S3上样本影像，打印图像的大小
img_body = dataset_interface.getImgXmlArray(img_files[0])
pil_image = Image.open(io.BytesIO(img_body))
print("image size:", pil_image.size)
```

输出结果：

```
Count of train image files: 1483
First train image file path: devel/101/dataset/recognition/49779ee7-1d00-4884-bf9a-dbc0802651e3/train/images/100_0.jpg
image size: (600, 600)
```

**（3）读取样本标签文件**

```python
# 根据影像的名称，获取对应的label文件路径
image_id = img_files[0].split('/')[-1].split('.')[0]
train_label_file = dataset_path + 'train/labels/%s.xml' % (image_id)
train_label_file = "/".join(train_label_file.split("/")[3:])
print(train_label_file)

# 获取标签xml内容
label_body = dataset_interface.getImgXmlArray(train_label_file)
print(label_body)
```

输出内容：

```
b'<annotation>\n  <folder>VOC</folder>\n  <filename>100_0.xml</filename>\n  <object_num>1</object_num>\n  <size>\n    <width>600</width>\n    <height>600</height>\n    <depth>3</depth>\n  </size>\n  <object>\n    <name>airplane</name>\n    <difficult></difficult>\n    <bndbox>\n      <xmin>124.0</xmin>\n      <xmax>249.0</xmax>\n      <ymin>172.0</ymin>\n      <ymax>291.0</ymax>\n    </bndbox>\n  </object>\n</annotation>\n'
```



#### 3.3 加载预训练模型

​	启动训练时可以选择任务下其他训练的结果模型或者中间模型作为预训练模型，如下所示：

![image-20210602180744384.png](https://i.loli.net/2021/06/03/FOkA8yhtcBmjzxN.png)

​	平台上结果模型和中间模型以对象存储形式保存在云端，选择预训练模型后会以云端url地址的形式传入，读取代码如下所示：

```python
# 定义YOLOv4的网络结构，获取网络结构的参数
model = YoloBody(len(anchors[0]), num_classes)
model_dict = model.state_dict()

# 定义下载到本地后预训练模型的存储路径
basedir = os.path.abspath(os.path.dirname(__file__))

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# 如果传入了预训练模型路径，加载预训练模型  
if args.resume_path:
    args.resume_path = "/".join(args.resume_path.split("/")[3:])
    # 下载云端预训练模型到本地
    dataset_interface.downS3Weight(basedir + '/' + args.model_name + ".th",
                                   args.resume_path + args.model_name + ".th")
    # 加载下载到本地的预训练模型
    pretrained_dict = torch.load(basedir + '/' + args.model_name + ".th", map_location=device)
    
    pretrained_dict = {k: v for k, v in pretrained_dict.items() if np.shape(model_dict[k]) == np.shape(v)}
    model_dict.update(pretrained_dict)
    model.load_state_dict(model_dict)
```



#### 3.4 训练过程的中间成果图片和模型输出

​	前端界面展示的每一个批次的中间成果，以及每一个epoch的模型需要输出到指定文件夹路径，平台会从默认路径中读取每一个epoch的中间成果图片用于前端渲染，同时将模型权重文件推送到云端进行存储（保证即使训练中出现异常，比如超时或代码异常导致的中断，也可以将本次训练的模型权重文件作为其他训练的预训练模型）。

​	平台指定的中间成果图片保存路径为/output/picture/，对于目标识别的训练，需要输出一张图片，命名为pred.png（预测结果框+原图），类似下图所示：

![image-20210603092153737.png](https://i.loli.net/2021/06/03/oIScBm3LXtK1V8U.png)

语义分割需要包含三张图片，命名为image.png（原始图片），label.png（标注图片），pred.png（训练中预测的图片），如下图所示：

![image-20210603092305742.png](https://i.loli.net/2021/06/03/eLIfQNMSGprgoKa.png)

变化检测需要包含四张图片，命名为A.png（变化前的图片），B.png（变化后的图片），label.png（标签图片）、pred.png（预测的图片），如下图所示：

![image-20210603092523229.png](https://i.loli.net/2021/06/03/2o95LBE3VcYpHN1.png)

​	模型权重文件的保存路径为/output/files，权重文件后缀为.th。

​	创建并保存中间成果的python代码参考如下所示：

```python
# 代码文件的根目录     
base_dir = os.path.abspath(os.path.dirname(__file__))

# 中间图片的输出目录
output_save_dir = base_dir + '/output/'

output_pic_dir = output_save_dir + 'picture/'
if not os.path.exists(output_pic_dir):
    os.makedirs(output_pic_dir)

# 中间模型权重文件的输出目录
output_file_dir = output_save_dir + 'files/'
if not os.path.exists(output_file_dir):
    os.makedirs(output_file_dir)
    
# 每一个epoch 输出中间结果
for epoch in range(0, args.epochs):
    # ...训练集样本训练
    
    # ...验证集样本训练
    # 保存该批次，验证集样本精度最高的预测图片，用于前端渲染展示
    img_png, label_png, pred_png = save_val_img()
    
    # 保存该批次训练的模型权重文件
    torch.save(model.state_dict(), output_file_dir + args.model_name + '.th')
    
    # Note: 重要该句提示平台当次epoch结束，需要推送中间结果到云端保存，否贼容易丢失中间成果
    print("[Process: {process}]".format(process=str(epoch + 1) + '/' + str(args.epochs)))
```



#### 3.5 指标详情文件输出格式规范

​	训练指标详情是通过日志的形式提供给前端进行展示的，日志文件名称约定为trainlog.json，具体示例如下：

```json
{
    "training_id": "57fc8152-c4f5-44b5-a25d-bc043a624d4b",
    "create_time": "2021-05-14 09:10:38",
    "description": {
        "recall": "召回率",
        "precision": "精度",
        "score": "得分",
        "IoU": "IoU",
        "loss": "损失率"
    },
    "epochs": [
        {
            "epoch": "1",
            "train": [
                {
                    "class": "all",
                    "values": {
                        "precision": 0.5015232918235704,
                        "recall": 0.5032873256241486,
                        "score": 0.3072759262049417,
                        "IoU": 0.1877801026848409,
                        "loss": 2.4991729259490967
                    }
                },
                {
                    "class": "backgroud",
                    "values": {
                        "precision": 0.10570210407760634,
                        "recall": 0.7237536292853153,
                        "score": 0.1844635853134588,
                        "IoU": 0.10160293608433331
                    }
                },
                {
                    "class": "bulding",
                    "values": {
                        "precision": 0.8973444795695344,
                        "recall": 0.28282102196298176,
                        "score": 0.43008826709642467,
                        "IoU": 0.2739572692853485
                    }
                }
            ],
            "valid": [
                {
                    "class": "all",
                    "values": {
                        "precision": 0.4971400360635547,
                        "recall": 0.4954240766711179,
                        "score": 0.24500841185249458,
                        "IoU": 0.1409498040396963,
                        "loss": 2.5524895191192627
                    }
                },
                {
                    "class": "backgroud",
                    "values": {
                        "precision": 0.10435099101877758,
                        "recall": 0.8066501379443454,
                        "score": 0.18479592664776257,
                        "IoU": 0.10180461407118782
                    }
                },
                {
                    "class": "bulding",
                    "values": {
                        "precision": 0.8899290811083319,
                        "recall": 0.18419801539789032,
                        "score": 0.3052208970572266,
                        "IoU": 0.18009499400820483
                    }
                }
            ]
        },
        {
            "epoch": "2",
            "train": [
                {
                    "class": "all",
                    "values": {
                        "precision": 0.5009439010949746,
                        "recall": 0.5019789923405797,
                        "score": 0.30923862390742596,
                        "IoU": 0.1888930809996141,
                        "loss": 2.479231834411621
                    }
                },
                {
                    "class": "backgroud",
                    "values": {
                        "precision": 0.10887003615274148,
                        "recall": 0.7213974681493446,
                        "score": 0.1891883602255373,
                        "IoU": 0.10447724530868183
                    }
                },
                {
                    "class": "bulding",
                    "values": {
                        "precision": 0.8930177660372076,
                        "recall": 0.28256051653181485,
                        "score": 0.42928888758931466,
                        "IoU": 0.2733089166905464
                    }
                }
            ],
            "valid": [
                {
                    "class": "all",
                    "values": {
                        "precision": 0.5006803840498844,
                        "recall": 0.5010988751210783,
                        "score": 0.24631657394517673,
                        "IoU": 0.1418360413403709,
                        "loss": 2.546833038330078
                    }
                },
                {
                    "class": "backgroud",
                    "values": {
                        "precision": 0.10454743231036989,
                        "recall": 0.8168058223043944,
                        "score": 0.18536833360318294,
                        "IoU": 0.10215216607280166
                    }
                },
                {
                    "class": "bulding",
                    "values": {
                        "precision": 0.8968133357893988,
                        "recall": 0.18539192793776224,
                        "score": 0.3072648142871705,
                        "IoU": 0.18151991660794015
                    }
                }
            ]
        }
    ],
    "best": {
        "precision": 0.4933007965322764,
        "recall": 0.48893562585985106,
        "score": 0.23985785670465115,
        "IoU": 0.1377504000404594
    },
    "end_time": "2021-05-14 10:51:20"
}
```

- **training_id**：本次训练的id号，训练启动时会传入，详见1.1

- **create_time**：训练的启动时间

- **description**：指标描述信息，每一种指标在前端展示的名称

- **epochs**：每一个批次的训练指标信息，包括批次号，训练集和验证集每一种类别的指标参数

- **best**：

- **end_time**：训练结束时间

  

  实现的python代码参考如下：

```python
# 定义log的格式
start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
log = {'training_id': args.training_id, 
       "create_time": start_time,
       "description": {"P":"精确度","R":"召回率","F1_score":"F1分数","mAP":"mAP"},
       "epochs": [], 
       "best": "", 
       "end_time": ""}

# 每一个epoch 输出指标信息
for epoch in range(0, args.epochs):
    epoch_log = {"epoch": str(epoch+1),
                 "train": [],
                 "valid": []}
    
    # 加入训练集指标
    epoch_log["train"].append({
        "class": "all",
        "values": {"P":train_mp, "R":train_mr, "F1_score":train_mf1, "mAP":train_map}})
    
    # 加入验证集指标
    epoch_log["valid"].append(
        {"class": "all", 
         "values": {"P": val_mp, "R": val_mr, "F1_score": val_mf1, "mAP": val_map}})
    
    log["epochs"].append(epoch_log)
    
    # 导出trainlog.json文件,导出文件夹outputSaveDir详见1.4
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log["end_time"] = end_time
    trainlog = json.dumps(log, indent=4)
    with open(outputSaveDir + 'trainlog' + '.json', 'w', encoding='utf-8') as log_file:
        log_file.write(trainlog)
```

