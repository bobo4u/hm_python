# 优化0819.py的代码

'''
1.之前的程序通过创建需要打印的列表以及一个打印的列表
2.每次打印以后，从需要打印去除，并转移到打印的类别（while程序实现）
3.需要打印列表pop一个，然后输出到正在打印中，然后append到已打印列表
--------------------------------------------------------

'''
# 定义两个函数，一个是负责出来打印的函数，一个是已经打印的函数

def print_models(weidayin,dayins):
    while weidayin:
        current = weidayin.pop()
        # print(f'Printing model:{current}')
        dayins.append(current)

def show_completed_models(dayins):
    print('已经打印的内容包括')
    for dayin in dayins:
        print(dayin)

weidayin = ['apple','house','car']
dayins = []

print_models(weidayin,dayins)
show_completed_models(dayins)