# contacts = [
#     {"姓名": "张三", "电话": "13800138000", "邮箱": "zhang@qq.com"},
# ]
# 1	查看所有	show_contacts()	空则提示。逐条 `1. 张三
# 2	添加	add_contact()	问三项，重名拒绝，电话必须纯数字，支持连续添加
# 3	搜索	search_contact()	输入关键词，姓名和电话都搜，模糊匹配（"张" in name）
# 4	修改	edit_contact()	选序号，只允许改电话和邮箱，越界保护
# 5	删除	delete_contact()	选序号，pop()，越界保护
# 6	统计	show_stats()	显示总人数 + 最长姓名是哪个
# 7	保存退出	save_contacts()	写 contacts.json
import os
import json

def contacts_read():
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r",encoding="utf-8") as file:
            return json.load(file)
    else:
        return []

contacts = contacts_read()

def save_contacts():
    with open("contacts.txt", "w",encoding="utf-8") as file:
        json.dump(contacts,file,ensure_ascii=True,indent=2)

def show_contacts():
        if not contacts:
            print("暂无联系人")
        else:
            for i in range(len(contacts)):
                print(f'{i+1}.{contacts[i]["姓名"]} {contacts[i]["电话"]} {contacts[i]["邮箱"]}')

def add_contacts():
    while True:
        while True:
            repetition_name = False
            name = input("姓名：")
            if not contacts:
                break
            for contact in contacts:
                if contact["姓名"] == name:
                    print("已有此人，请勿重复添加")
                    repetition_name = True
            if repetition_name:
                continue
            else:
                break
        while True:
            phone = input("电话：")
            if phone.isdigit() | len(phone) == 11:
                break
            else:
                print("电话格式错误，应为11位纯数字")
                continue
        emile = input("邮箱：")
        contacts.append({"姓名":name,"电话":phone,"邮箱":emile})
        if input("请输入：1.结束 2.继续 ") == "1":
            save_contacts()
            break
        else:
            continue






