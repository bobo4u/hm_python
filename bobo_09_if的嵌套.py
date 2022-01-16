has_ticket = True
knife_length = 6
if has_ticket:
    print("有车票，请开始安检")
    if knife_length > 20:
        print("携带危险道具，有%d公分长\n禁止上车"% knife_length)
    else:
        print("安检通过，祝您旅途愉快")
else:
    print("请安检")