import re


log = """2024-01-01 10:30:45 192.168.1.1 GET /index.html
2024-01-01 10:31:12 10.0.0.5 POST /login
2024-01-01 10:32:01 192.168.1.1 GET /about
2024-01-01 10:33:45 172.16.0.8 GET /contact
2024-01-01 10:34:01 10.0.0.5 GET /about
2024-01-01 10:35:12 10.0.0.5 GET /index.html
2024-01-01 10:36:45 192.168.1.1 POST /login
2024-01-01 10:37:01 172.16.0.8 GET /contact"""


contacts = re.findall(r"\d+\.\d+\.\d+\.\d+", log)
# ip_count = {IP地址: 出现次数}
ip_count = {}
for contact in contacts:
    if contact not in ip_count:
        ip_count[contact] = 0          # 第一次见，初始 0
    ip_count[contact] += 1              # 计数 +1

ip_sorted = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)
for i in ip_sorted:
    print(f'{i[0]}: {i[1]} 次')



