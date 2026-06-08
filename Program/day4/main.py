# 查看所有	显示 1. [高] 买菜 — 未完成
# 添加	问标题+优先级（高/中/低），默认"未完成"
# 完成	选序号，把状态改成"已完成"
# 删除	选序号删除，加越界保护
# 按优先级排序	高→中→低显示（提示：先把"高"的放到一个新列表，再放"中"的，再放"低"的）
# 退出	拜拜

print("=" * 20, "待办事项管理系统", "=" * 20)
todos = []
print("菜单：1.查看所有 2.添加 3.完成 4.删除 5.按优先级排序 6.退出")
while True:
    num = int(input("选择功能："))
    if num == 1:
        print("=" * 20, "查看所有", "=" * 20)
        if not todos:
            print("暂无事项")
        else:
            for task in todos:
                print(f'{task["序号"]}.{task["任务"]}：{task["完成情况"]} {task["等级"]}')
    elif num == 2:
        print("=" * 20, "添加任务", "=" * 20)
        while True:

            task_num = str(len(todos) + 1)
            task_name = input("请输入任务名称：")
            task_title = input("请输入任务等级：")
            todos.append({"序号": task_num, "任务": task_name, "等级": task_title, "完成情况": "未完成"})

            num = input("继续输入：1，结束输入：2 ：")
            if num == "1":
                continue
            else:
                break
    elif num == 3:
        print("=" * 20, "完成任务", "=" * 20)
        while True:
            if not todos:
                print("暂无任务")
            else:
                task_name = input("请输入完成任务名称")
                found = False
                for task in todos:
                    if task["任务"] == task_name:
                        task["完成情况"] = "已完成"
                        found = True
                        print(f"✅ {task_name} 已完成")
                if not found:
                    print("没找到这个任务")

            num = input("继续输入：1，结束输入：2 ：")
            if num == "1":
                continue
            else:
                break

    elif num == 4:
        print("=" * 20, "删除任务", "=" * 20)
        while True:
            if not todos:
                print("暂无任务")
            else:
                task_num = int(input("请输入要删除第几个任务："))
                if 1 <= task_num <= len(todos):
                    done = todos.pop(task_num - 1)
                    print(f'✅ 已删除：{done["任务"]}')
                else:
                    print("序号不存在！")

            num = input("继续输入：1，结束输入：2 ：")

            if num == "1":
                continue
            else:
                break

    elif num == 5:
        low = []
        middle = []
        high = []
        print("=" * 20, "任务排序", "=" * 20)
        if not todos:
            print("暂无任务")
        else:

            for task in todos:
                if task["等级"] == "高级":
                    high.append(task)
                elif task["等级"] == "中级":
                    middle.append(task)
                elif task["等级"] == "低级":
                    low.append(task)

            todos.clear()

            if not high:
                print("无高级任务")
            else:
                for task in high:
                    todos.append(task)
            if not middle:
                print("无中级任务")
            else:
                for task in middle:
                    todos.append(task)
            if not low:
                print("无低级任务")
            else:
                for task in low:
                    todos.append(task)

        for task in todos:
            print(f'{task["序号"]}.{task["任务"]}：{task["完成情况"]} {task["等级"]}')
    elif num == 6:
        print("拜拜")
    else:
        print("输入功能序号错误，请重新选择")
        continue






