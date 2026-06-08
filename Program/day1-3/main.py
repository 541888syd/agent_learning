names = []
scores = []
print("======================成绩管理系统===========================")
while True:
    print("菜单：1.查看所有 2.添加 3.平均分 4.最高分 5.删除 6.退出")
    num = int(input("请选择功能："))
    if num == 1:
        print("========================查看所有=========================")
        if not names:
            print("暂无成绩")
        else:
            for i in range(len(names)):
                print(f"{i+1}.{names[i]}:{scores[i]}分")
    elif num == 2:
        print("=========================添加===========================")
        while True:
            name = input("姓名：")
            score = int(input("成绩："))
            if score < 0 or score > 100:
                print("无效成绩，重新输入")
                continue
            else:
                names.append(name)
                scores.append(score)
                print("添加成功")
                for i in range(len(names)):
                    print(f"{i+1}.{names[i]}:{scores[i]}")
                if input("继续：yes 退出：esc 请选择：") == "yes":
                    continue
                else:
                    break
    elif num == 3:
        print("=========================平均分========================")
        if not names:
            print("暂无成绩")
        else :
            print(f"平均分：{sum(scores)/len(scores)}")
    elif num == 4:
        print("=========================最高分========================")
        max_score = max(scores)
        for i in range(len(scores)):
            if max_score == scores[i]:
                print(f"{i+1}.{names[i]}:{scores[i]}分")
    elif num == 5:
        print("==========================删除=========================")
        while True:
            for i in range(len(names)):
                print(f"{i + 1}.{names[i]}:{scores[i]}分")
            delete = int(input("请选择删除哪一个："))
            if delete < 1 or delete>len(names):
                print(f"输入序号无效，共有{len(names)}人成绩，请重新输入")
                continue
            else:
                names.remove(names[delete-1])
                scores.remove(scores[delete-1])
                print("删除成功")
                for i in range(len(names)):
                    print(f"{i + 1}.{names[i]}:{scores[i]}分")
                if input("继续：yes 退出：esc 请选择：") == "yes":
                    continue
                else:
                    break
    elif num == 6:
        print("拜拜")
        break
