# 关键字with在不再需要访问文件后将其关闭。否则需要调用open和close来打开和关闭文件。
with open('guest_book.txt') as file_object:
    contents = file_object.read()

print(contents)
# print(contents.rstrip())