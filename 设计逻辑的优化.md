# 创建列表，包含要打印的内容

```
weidayin = ['apple','house','car']
dayins = []
```
#打印每个设计，并转移到dayin的列表中

```
while weidayin:
    current = weidayin.pop()
    print(f'Printing model: {current}')
    dayins.append(current)
```
# 显示已经打印的内容
```
for dayin in dayins: 
    print(dayin)
```