# 判断字符串中是否只包含数字

num_str = "1"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())


hello_str = "hello world"
# replace方法执行以后会返回一个新的字符串
# 不会修改原有字符串的内容
print(hello_str.replace("world","python"))

print(hello_str.find("world"))
print(hello_str.index("hello"))