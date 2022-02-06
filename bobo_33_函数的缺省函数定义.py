

def print_info(name,gender = True):
    """
    name:班上同学的姓名
    gender :True 男生 False 女生
        
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name,gender_text))


print_info("小明")

print_info("小妹",False)