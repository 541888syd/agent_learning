# \d	digit	一个数字 0-9
# \d+	digit +	一个或多个数字
# \w	word character	字母、数字、下划线
# \s	space	空白符（空格/换行/制表符）
# .		任意一个字符
# \.	真正的点号（反斜杠转义）
# + 	前面的东西出现 1 次或多次
# *	    前面的东西出现 0 次或多次


# 2024-01-01 10:30:45 192.168.1.1 GET /index.html
# 2024-01-01 10:31:12 10.0.0.5 POST /login
# 2024-01-01 10:32:01 192.168.1.1 GET /about
# 2024-01-01 10:33:45 172.16.0.8 GET /contact


# 时间: 2024-01-01 10:30:45, IP: 192.168.1.1
# 时间: 2024-01-01 10:31:12, IP: 10.0.0.5
# 时间: 2024-01-01 10:32:01, IP: 192.168.1.1
# 时间: 2024-01-01 10:33:45, IP: 172.16.0.8
#
# 所有IP: ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.8']
import re

log = """2024-01-01 10:30:45 192.168.1.1 GET /index.html
2024-01-01 10:31:12 10.0.0.5 POST /login
2024-01-01 10:32:01 192.168.1.1 GET /about
2024-01-01 10:33:45 172.16.0.8 GET /contact"""

split_log = log.split("\n")

for line in log.split("\n"):
    spilt_line = line.split(" ")
    print(f'时间: {spilt_line[0]} {spilt_line[1]}, IP: {spilt_line[2]}')
ip = re.findall(r"\d+\.\d+\.\d+\.\d+", log)
print(f'所有IP: {ip}')

new_log = log.replace("GET", "FETCH")
print(new_log)
