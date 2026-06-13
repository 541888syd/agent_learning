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
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r",encoding="UTF-8") as file:
            return json.load(file)
    else:
        return []


def save_contacts():
    with open("contacts.json", "w",encoding="UTF-8") as file:
        json.dump(contacts,file,ensure_ascii=False,indent=2)
        print("已保存到本地")


# 1	查看所有	show_contacts()	空则提示。逐条 `1. 张三
def show_contacts():
        if not contacts:
            print("暂无联系人")
        else:
            for i in range(len(contacts)):
                print(f'{i+1}.{contacts[i]["姓名"]} {contacts[i]["电话"]} {contacts[i]["邮箱"]}')

# 2	添加	add_contact()	问三项，重名拒绝，电话必须纯数字，支持连续添加
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
            if phone.isdigit() and len(phone) == 11:
                break
            else:
                print("电话格式错误，应为11位纯数字")
                continue
        emile = input("邮箱：")
        contacts.append({"姓名":name,"电话":phone,"邮箱":emile})
        if input("请输入：1.结束 2.继续 ") == "1":
            save_contacts()
            break


# 3	搜索	search_contact()	输入关键词，姓名和电话都搜，模糊匹配（"张" in name）
def search_contact():
    if not contacts:
        print("暂无联系人")
    else:
        keyword  = input("请输入姓名中任意字，或者输入手机号任意几位数字：")
        search_result = []

        for contact in contacts:
            if keyword in contact["姓名"] or keyword in contact["电话"]:
                search_result.append(contact)

        if len(search_result) != 0:
            print(f'共搜索到{len(search_result)}条人员信息')

            for m,search_result in enumerate(search_result,1):
                print(f'{m}.{search_result["姓名"]} {search_result["电话"]} {search_result["邮箱"]}')
        else:
            print("未搜索到相关人员信息")


# 4	修改	edit_contact()	选序号，只允许改电话和邮箱，越界保护
def edit_contact():
    if not contacts:
        print("暂无联系人")
    else:
        while True:
            num = input("请输入您想修改的人员序号或退出（esc）：")
            if num.isdigit() and 0 <= int(num) <= len(contacts):
                for i, contact in enumerate(contacts,1):
                    if int(num) == i:
                        while True:
                            print(f'{i}.{contact["姓名"]} {contact["电话"]} {contact["邮箱"]}')
                            input_contact = input("请输入您想修改的内容（电话/邮箱）或退出（esc）：")
                            if input_contact == "电话":
                                while True:
                                    phone = input("请输入新的11位数字电话号：")
                                    if phone.isdigit() and len(phone) == 11:
                                        contact["电话"] = phone
                                        print("修改电话成功")
                                        break
                                    else:
                                        print("电话格式错误请")
                                continue

                            elif input_contact == "邮箱":
                                email = input("请输入邮箱：")
                                contact["邮箱"] = email
                                print("修改邮箱成功")

                            elif input_contact == "esc":
                                break

                            else:
                                print("无此项内容，请重新选择输入项：")
            elif num == "esc":
                break
            else:
                print("无此序号人员，请重新确认序号")
                continue

# 5	删除	delete_contact()	选序号，pop()，越界保护
def delete_contact():
    if not contacts:
        print("暂无联系人")
    else:
        while True:
            for i, contact in enumerate(contacts, 1):
                print(f'{i}.{contact["姓名"]} {contact["电话"]} {contact["邮箱"]}')
            num = input("请输入您想删除的人员序号或退出（esc）：")
            if num.isdigit() and int(num) <= len(contacts):
                for i, contact in enumerate(contacts,1):
                    if int(num) == i:
                        contacts.pop(i-1)
                        print("已删除")
                continue
            elif num == "esc":
                break
            else:
                print("无此序号人员，请重新选择输入项：")
# 6	统计	show_stats()	显示总人数 + 最长姓名是哪个
def show_stats():
    if not contacts:
        print("暂无联系人")
    else:
        max_name = 0
        long_name = []
        for i,contact in enumerate(contacts,1):
            long_num = len(contact["姓名"])
            if long_num > max_name:
                max_name = long_num
        for contact in contacts:
            if len(contact["姓名"]) == max_name:
                long_name.append(contact["姓名"])

        print(f'总人数为：{len(contacts)},姓名最长为{max_name}个字，姓名长度排名第一的为{long_name}')



contacts = contacts_read()
while True:
    function = input("请输入功能序号：1.查看所有 2.添加 3.搜索 4.修改 5.删除 6.统计 7.退出：")
    if function == "1":
        show_contacts()
    elif function == "2":
        add_contacts()
    elif function == "3":
        search_contact()
    elif function == "4":
        edit_contact()
    elif function == "5":
        delete_contact()
    elif function == "6":
        show_stats()
    elif function == "7":

        save_contacts()
        break
    else:
        print("无此功能，请重新选择")





