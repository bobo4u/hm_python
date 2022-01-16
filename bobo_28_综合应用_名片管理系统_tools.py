# 纪录名片字典
card_list = []

def show_menu():
    
    """显示菜单"""
    print("*" * 50)
    print("欢迎登录名片管理系统")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")

    print("*" * 50)

def new_card():

    """新增名片"""
    print("*" * 25)
    print("新增名片")

    # 1.输入名片信息
    name_str = input("请输入姓名: ")
    phone_str = input("请输入电话: ")
    QQ_str = input("请输入QQ: ")
    email_str = input("请输入邮箱: ")

    # 2.建立名片字典
    card_dict = {"Name":name_str,
                 "Phone":phone_str,
                 "QQ":QQ_str,
                 "Email":email_str}
    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示用户添加成成功
    print("添加 %s 的名片成功" % name_str)


def show_all():

    """显示所有名片"""
    print("~" * 25)
    print("显示所有名片信息")
    # 判断是否有名片
    if len(card_list) == 0:

        print("当前没有名片")

        # 下方的代码不会被执行 
        # return 后面没有任何内容 返回调用函数的位置
        return

    # 打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")
    # 换行
    print("")
    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["Name"],
                                        card_dict["Phone"],
                                        card_dict["QQ"],
                                        card_dict["Email"]))
    print("=" * 50)


def serch_card():

    """搜索名片"""
    print("*" * 25)
    print("搜索名片")


    # 输入搜索的姓名
    find_name = input("请输入要查找的姓名:  ")
    
    # 遍历名片列表
    for card_dict in card_list:
        if card_dict["Name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["Name"],
                                        card_dict["Phone"],
                                        card_dict["QQ"],
                                        card_dict["Email"]))
            # 调用处理名片的函数
            deal_card(card_dict)            
            
            break
    else:
        print("抱歉，没有找到 %s " % find_name)


def deal_card(find_dict):
    """修改或者删除查找到的名片"""

    acction_str = input("请输入操作 1 修改 2 删除 0 返回操作")
    if acction_str == "1":


        find_dict["Name"] = input_card_info( find_dict["Name"],"姓名: ")
        find_dict["Phone"] = input_card_info( find_dict["Phone"],"电话: ")
        find_dict["QQ"] = input_card_info( find_dict["QQ"],"QQ: ")
        find_dict["Email"] = input_card_info( find_dict["Email"],"邮箱: ")

        print("修改") 
    elif acction_str == "2":
        card_list.remove(find_dict)

        print("删除名片成功")

def input_card_info(find,message):
    """修改名片"""
    # 提示输入
    result_str = input(message)
    # 输入内容进行判断
    if len(result_str) > 0:
        return result_str
    # 如果没有输入 返回原有的值
    else:

        return find



