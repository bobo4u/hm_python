import bobo_28_综合应用_名片管理系统_tools

while True:

    # TODO 完善后续功能
    bobo_28_综合应用_名片管理系统_tools.show_menu()

    action_str = input("请选择操作功能:")
    print("您选择的操作是【%s】"% action_str)

    # 针对1,2,3的操作
    if action_str in ["1","2","3"]:

        if action_str == "1":
            bobo_28_综合应用_名片管理系统_tools.new_card()
        elif action_str == "2":
            bobo_28_综合应用_名片管理系统_tools.show_all()
        elif action_str == "3":
            bobo_28_综合应用_名片管理系统_tools.serch_card()
    
        # 不希望立刻编写分支内部的代码
        # 可以使用pass关键字，作为占位符，确保程序的代码结果正确
        # pass


    elif action_str == "0":

        print("欢迎再次使用[名片管理系统]")

        break

    else:
        print("您输入的不正确，请重新输入")