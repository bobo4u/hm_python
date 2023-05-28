responses = {}
active = True

while active:
    name = input('请输入你的名称')
    response = input('你明天打算爬山吗')
    # 将答案存储在字典中
    responses[name] = response

    repeat = input('还有同学有回答吗？yes/no')
    if repeat == 'no':
        active = False

print('\n---- Poll Results---')
for name,response in responses.items():
    print(f'{name} would like to climb {response}.')
