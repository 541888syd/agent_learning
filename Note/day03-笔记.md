# Day 3 笔记：列表 + for 循环

---

## 1. 什么是列表

一个变量装一堆东西，用 `[]` 包裹，逗号分隔。

```python
names = ["小明", "小红", "小刚"]
nums = [1, 2, 3, 4, 5]
empty = []          # 空列表
```

---

## 2. 索引从 0 开始

```
列表： ["苹果", "香蕉", "橘子"]
索引：    0       1       2
```

```python
fruits = ["苹果", "香蕉", "橘子"]
print(fruits[0])    # 苹果
print(fruits[-1])   # 橘子（-1 = 倒数第一个）
```

---

## 3. 增删改查

| 操作 | 代码 | 效果 |
|------|------|------|
| 加末尾 | `列表.append(x)` | x 加到列表最后 |
| 查存在 | `x in 列表` | 返回 True/False |
| 按内容删 | `列表.remove(x)` | 删掉第一个匹配的 x |
| 按位置删 | `列表.pop(i)` | 删掉索引 i，返回被删元素 |
| 改 | `列表[i] = x` | 把索引 i 改成 x |
| 个数 | `len(列表)` | 返回元素个数 |
| 是空？ | `if not 列表:` | 空列表 = True |
| 最大 | `max(列表)` | 返回最大值 |
| 最小 | `min(列表)` | 返回最小值 |
| 求和 | `sum(列表)` | 返回总和 |

---

## 4. ⚠️ remove() vs pop() 的坑

```python
names = ["小明", "小红", "小明"]
scores = [85, 90, 70]

# ❌ remove() 按「内容」删除 — 有重复内容时会删错！
names.remove("小明")    # 删的是第1个

# ✅ pop() 按「位置」删除 — 精准！
names.pop(2)            # 删的是第3个
```

**规则**：删除明确位置的东西用 `pop()`，不要用 `remove()`。

---

## 5. for 循环遍历列表

```python
fruits = ["苹果", "香蕉", "橘子"]

# 直接拿元素
for fruit in fruits:
    print(fruit)

# 带编号
for i in range(len(fruits)):
    print(f"{i+1}. {fruits[i]}")
```

---

## 6. range() 用法

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

---

## 7. break 和 continue

```python
for i in range(1, 6):
    if i == 3:
        break       # 直接结束整个循环
    print(i)
# 输出：1 2

for i in range(1, 6):
    if i == 3:
        continue    # 跳过本次，继续下一轮
    print(i)
# 输出：1 2 4 5
```

```python
while True:
    cmd = input("命令：")
    if cmd == "quit":
        break       # 跳出循环，程序结束
    if cmd == "":
        continue    # 跳回 while 顶部重新等输入
    print(f"执行：{cmd}")
```

| | 效果 | 比喻 |
|---|------|------|
| `break` | 结束整个循环 | 下课铃响，直接放学 |
| `continue` | 跳过本轮 | 这道不会，做下一道 |

---

## 8. 注释

```python
# 单行注释用井号

"""
多行注释
用三个引号
"""
```

---

## 9. 两个列表配对模式

当数据有关联时（如姓名和成绩），用同一个索引：

```python
names = ["小明", "小红"]
scores = [85, 90]

names[0] 和 scores[0] 对应同一个人
names[1] 和 scores[1] 对应同一个人
```

操作时两个列表**同步操作**：
- 添加：两个列表同时 append
- 删除：两个列表同位置 pop
- 遍历：同一个 i 同时取两个列表

---

## 10. 常见坑

| 坑 | 原因 | 怎么避免 |
|----|------|----------|
| `max([])` 报错 | 不能对空列表求最大值 | 先 `if not list:` 判空 |
| `remove()` 删错 | 有重复内容 | 用 `pop()` 按位置删 |
| `IndexError` 越界 | 索引超出范围 | `if 1 <= n <= len(list):` 保护 |
| 缩进混乱 | 空格/Tab混用 | 用 VS Code 统一缩进 |
| 忘记初始化 | 变量没定义就用了 | 循环前加 `list = []` |

---

## 11. 练习参考答案

### 待办事项管理器
```python
todos = []

while True:
    num = int(input("\n1.查看 2.添加 3.完成 4.退出\n请选择："))

    if num == 1:
        if not todos:
            print("暂无待办")
        else:
            for i in range(len(todos)):
                print(f"{i+1}. {todos[i]}")

    elif num == 2:
        task = input("新事项：")
        todos.append(task)
        print(f"✅ 已添加：{task}")

    elif num == 3:
        if not todos:
            print("无待办可删")
        else:
            for i in range(len(todos)):
                print(f"{i+1}. {todos[i]}")
            n = int(input("完成第几个："))
            if 1 <= n <= len(todos):
                print(f"✅ 已完成：{todos.pop(n-1)}")
            else:
                print("序号无效！")

    elif num == 4:
        print("拜拜！")
        break
```

### 成绩管理器
```python
names = []
scores = []

while True:
    print("\n1.查看 2.添加 3.平均分 4.最高分 5.删除 6.退出")
    num = int(input("请选择："))

    if num == 1:
        if not names:
            print("暂无成绩")
        else:
            for i in range(len(names)):
                print(f"{i+1}. {names[i]}：{scores[i]}分")

    elif num == 2:
        while True:
            name = input("姓名：")
            score = int(input("成绩："))
            if score < 0 or score > 100:
                print("成绩无效，0-100之间")
                continue
            names.append(name)
            scores.append(score)
            print("✅ 添加成功")
            if input("继续？(yes/esc)：") != "yes":
                break

    elif num == 3:
        if not names:
            print("暂无成绩")
        else:
            avg = sum(scores) / len(scores)
            print(f"平均分：{avg:.1f}")

    elif num == 4:
        if not names:
            print("暂无成绩")
        else:
            best = max(scores)
            for i in range(len(names)):
                if scores[i] == best:
                    print(f"🥇 {names[i]}：{scores[i]}分")

    elif num == 5:
        if not names:
            print("暂无成绩可删")
        else:
            for i in range(len(names)):
                print(f"{i+1}. {names[i]}：{scores[i]}分")
            n = int(input("删除第几个："))
            if 1 <= n <= len(names):
                print(f"✅ 已删除：{names.pop(n-1)}")
                scores.pop(n-1)
            else:
                print("序号无效！")

    elif num == 6:
        print("拜拜！")
        break
```

---

## ✅ Day 3 检查清单

- [ ] 会创建列表、按索引取值
- [ ] 会用 append / pop / in / len / max / min / sum
- [ ] 会判断列表为空 `if not list:`
- [ ] 能用 for 遍历列表（直接 / 带编号）
- [ ] 会用 range()
- [ ] 理解 break 和 continue 的区别
- [ ] 知道 remove 的坑，优先用 pop
- [ ] 能操作两个配对列表
- [ ] 独立完成待办事项管理器 + 成绩管理器
