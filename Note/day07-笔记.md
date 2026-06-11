# Day 7 笔记：通讯录管理系统（第1周综合项目）

> 日期：2026-06-11 | 状态：进行中 ✍️

---

## 一、、isdigit() — 判断字符串是否纯数字

```python
"13800138000".isdigit()    # True  全是数字
"138x".isdigit()           # False 含非数字字符
"".isdigit()               # False 空字符串也返回 False
```

**用途**：验证电话号码必须为纯数字。

```python
phone = input("电话：")
if phone.isdigit() and len(phone) == 11:
    print("合法")
```

---

## 二、break 只管最近那一层循环

```python
while True:                          # 外层循环
    name = input("姓名：")
    for contact in contacts:         # 内层循环
        if contact["姓名"] == name:
            print("重复！")
            break                    # ← 跳出 for，不是跳出 while！
    phone = input("电话：")           # ← 仍然执行！
```

**解决**：用标记变量配合 `continue`：

```python
duplicated = False
for contact in contacts:
    if contact["姓名"] == name:
        duplicated = True
        break              # 跳出 for

if duplicated:
    continue               # 跳过本轮 while，回到 name 输入
# 没重复才继续问电话
```

---

## 三、逻辑运算符 and / or（不是 | / &）

| Python 逻辑 | Python 位运算 | 意思 |
|:-----------:|:----------:|------|
| `and` | `&` | 两边都为 True |
| `or` | `&#124;` | 任意一边为 True |
| `not` | `~` | 取反 |

```python
# ❌ | 是位运算，结果不是你想要的
if phone.isdigit() | len(phone) == 11:

# ✅ and / or 才是逻辑判断
if phone.isdigit() and len(phone) == 11:
```

---

## 四、json.dump() ensure_ascii 参数

```python
# ensure_ascii=True（默认）→ 中文变乱码
json.dump(data, f)                  # {"name": "\u5c0f\u660e"}

# ensure_ascii=False → 中文正常显示
json.dump(data, f, ensure_ascii=False)  # {"name": "小明"}
```

---

## 五、标记变量模式（flag pattern）

当需要在循环中记录"是否发生过某件事"，用布尔变量：

```python
found = False
for item in items:
    if 匹配条件:
        found = True
        break

if found:
    # 找到了，做处理
else:
    # 没找到，做另一件事
```

---

## 六、嵌套 while True 结构

```python
while True:                    # 主添加循环（可连续添加多人）
    while True:                # 姓名输入循环（重名就重输）
        # 重名检查
        if 通过:
            break
    while True:                # 电话输入循环（格式错就重输）
        # 格式检查
        if 通过:
            break
    # 邮箱
    # 添加到列表
    if 不想继续:
        break                  # 跳出主添加循环
```

---

## 七、项目结构规范

```
1. import 语句
2. 函数定义（所有功能函数）
3. 全局变量 + 启动加载
4. 主循环（只调度函数，不写功能代码）
```

---

## ✅ 今日易错清单

| 错误 | 原因 | 正确 |
|------|------|------|
| `if a | b:` | `|` 是位运算不是逻辑或 | `if a or b:` |
| `break` 想退出外层 | break 只管最近一层 | 标记变量 + continue |
| `ensure_ascii=True` | 中文变 Unicode 编码 | `ensure_ascii=False` |
| `.isdigit()` 测空串 | 空字符串返回 False | 先判空再测 |
