# 创建aliens的空列表
aliens = []
# 创建30个绿颜色的alien
for alien_number in range(30):
    new_alien = {"color":"green","points":5,"speed":"slow"}
    aliens.append(new_alien)
    # print(type(new_alien))
    # print(type(aliens))
for alien in aliens[:2]:
    if alien["points"] == 5 :
        alien["color"] = "red"
        alien["points"] = 10
        # alien["speed"] = "medium"
        print(alien["points"])

for alien in aliens[:5]:
    print(alien)
    print(alien["color"])