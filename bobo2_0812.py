un_users = ['alice','brain','candace']

confirmed_users = []

while un_users:
    # 从列表末尾删除一个用户
    current_user = un_users.pop()
    print(f'Verifying user:{current_user.title()}')
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print(f'\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())