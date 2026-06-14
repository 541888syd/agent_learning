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
contacts = ["苹果","香蕉","橘子","苹果"] #初始化
for m in contacts:
    print(m)

# 列表的操作函数：
# 常用的增删查改
contacts.append("狗屎") #在后面添加
contacts.pop(0) #按序号删除
contacts.remove("苹果") #按内容删除（遇到的第一个）
print("香蕉" in contacts) #返回True和False
contacts[1] = "牛皮" # 修改此序号对应数值

contacts_len = len(contacts) #获取长度函数
# 后两个输出一样，但是enumerate更简洁
for i in range(0,contacts_len):
    print(f'{i+1}.{contacts[i]}')

for i,m in enumerate(contacts,1):
    print(f'{i}.{m}')


# day4:
# 字典

# day5:
# 函数

# day6:
# json数据存储