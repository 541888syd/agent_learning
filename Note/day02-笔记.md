# Day 2 笔记：判断 + 循环

---

## 1. if/else — 让程序做判断

```python
if 条件:
    条件成立做的事
else:
    条件不成立做的事
```

**例子**：
```python
weather = "下雨"
if weather == "下雨":
    print("带伞")
else:
    print("不带")
```

---

## 2. 比较符号

| 符号 | 意思 | 例子 | 结果 |
|------|------|------|------|
| `==` | 等于 | `5 == 5` | `True` |
| `!=` | 不等于 | `5 != 3` | `True` |
| `>` | 大于 | `5 > 3` | `True` |
| `<` | 小于 | `5 < 3` | `False` |
| `>=` | 大于等于 | `5 >= 5` | `True` |
| `<=` | 小于等于 | `3 <= 5` | `True` |

⚠️ `==` 是比较，`=` 是赋值，别搞混！

---

## 3. elif — 多条件判断

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 70:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

从上往下检查，**第一个成立的执行，后面跳过**。

---

## 4. while — 重复执行

```python
while 条件:
    条件成立时重复做的事
```

**关键**：循环里必须改变条件，否则**死循环**！

```python
count = 1
while count <= 5:
    print(f"第{count}次")
    count = count + 1      # ← 必须有这行！
```

---

## 5. import random — 生成随机数

```python
import random
num = random.randint(1, 100)   # 1到100之间的随机整数
```

---

## 6. 练习：猜数字游戏

```python
import random

answer = random.randint(1, 100)
guess = 0
times = 0

print("我想好了一个1到100之间的数字，你猜猜看？")

while guess != answer:
    guess = int(input("你猜："))
    times = times + 1

    if guess > answer:
        print("大了！")
    elif guess < answer:
        print("小了！")
    else:
        print(f"恭喜！你猜了{times}次就猜对了！")
```

---

## 7. 缩进规则

```python
while guess != answer:           # 这行是while的"领地入口"
    guess = int(input("你猜："))  # ← 缩进4格 = 归while管
    times = times + 1             # ← 缩进4格 = 也归while管

    if guess > answer:            # ← 缩进4格 = 归while管
        print("大了！")            # ← 缩进8格 = 归if管
    elif guess < answer:          # ← 缩进4格 = 归while管
        print("小了！")            # ← 缩进8格 = 归if管
```

Python 用缩进区分层级，**同一级缩进必须一致**。

---

## ✅ Day 2 检查清单

- [ ] 会用 `if/elif/else` 做判断
- [ ] 分得清 `==`（比较）和 `=`（赋值）
- [ ] 会用 `while` 写循环
- [ ] 知道什么是死循环，怎么避免
- [ ] 会用 `import random` 生成随机数
- [ ] 能独立写出猜数字游戏
- [ ] 理解缩进的作用
