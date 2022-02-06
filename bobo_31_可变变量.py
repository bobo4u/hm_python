from turtle import pensize


def demo(num_list):

    print("函数内部的代码")


    num_list.append(19)

    print(num_list)

    print("函数执行完成")

gl_list = [1,2,3] 

demo(gl_list)

print(gl_list)