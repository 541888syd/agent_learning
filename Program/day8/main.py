import os
import json
# day1:
# 输入输出
print("你好")
name = input("姓名：")
print(f'姓名：{name}')

# day2:
# 判断循环
if name == "wang":
    print("wang")
# range(0,2):0,1 从0开始到5之前停下
for i in range(0,2):
    print(i)
# 随机数函数:
import random #随机库
# 随机整数函数
random.randint(0,100) #从0到100选个随机整数


# day3:
# 列表
contact = ["苹果","香蕉","橘子","苹果"] #初始化
for m in contact:
    print(m)

# 列表的操作函数：
# 常用的增删查改
contact.append("狗屎") #在后面添加
contact.pop(0) #按序号删除
contact.remove("苹果") #按内容删除（遇到的第一个）
print("香蕉" in contact) #返回True和False
contact[1] = "牛皮" # 修改此序号对应数值

contact_len = len(contact) #获取长度函数
# 后两个输出一样，但是enumerate更简洁
for i in range(0,contact_len):
    print(f'{i+1}.{contact[i]}')

for i,m in enumerate(contact,1):
    print(f'{i}.{m}')

# 列表：只有值（只按序号来取），同一属性的多个东西：水果列表：["苹果","香蕉","橘子","苹果"]
# 字典：有键名（所谓的标签），一个人东西的多个属性：人物信息：{"性别":"男","姓名":"王八蛋","性格":"温柔"}
# 字典列表：列表内的元素是字典，多个人的多个的同一属性：人物信息表：[{"性别":"男","姓名":"王八蛋","性格":"温柔"},{"性别":"女","姓名":"丫蛋","性格":"温柔"}]

# day4:
# 字典
contacts = {"性别":"男","姓名":"王八蛋","性格":"温柔"}


print(list(contacts.keys()))                # 所有键：["姓名", "年龄"]
print(list(contacts.values()))              # 所有值：["张三", 25]
print(list(contacts.items()))               # 键值对：[("姓名","张三"), ("年龄",25)]

# 常用操作函数增删查改：
contacts["喜好"] = "零食"
contacts.pop("性别") #按键名
print("姓名" in contacts)
contacts["姓名"] = "狗"

# day5:
# 函数

# day6:
# json数据存储

if os.path.exists("contacts.json"): # 路径是否存在contacts.json文件
    with open("contacts.json","r",encoding="utf-8") as f: # 打开 contacts.json，只读模式，UTF-8 编码，给它起个名叫 f，用完自动关。
        contacts = json.load(f) # 将文件内容转换成python能懂的字典或列表

with open ("contacts.json","w",encoding="utf-8") as f: # 打开 contacts.json，只写模式，UTF-8 编码，给它起个名叫 f，用完自动关。

    # 将contacts转换成ensure_ascii=False,indent=4的json格式文件存到f   ensure_ascii=False → 中文正常显示   indent=4 → 缩进 4 格
    json.dump(contacts,f,ensure_ascii=False,indent=4)