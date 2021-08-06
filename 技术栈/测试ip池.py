import random
import requests
import re

'''
利用访问http://icanhazip.com/返回的IP进行测试
说明：利用的http://icanhazip.com/返回的IP进行校验，如返回的是代理池的IP，说明代理有效，否则实际代理无效
'''

# 代理ip池
PROXIES_NEW = {
    "https": [
        "https://113.226.18.243:80",
        "https://121.31.100.209:8123",
        "https://14.117.177.135:808",
        "https://171.223.230.46:61234",
        "https://117.57.90.121:25435",
        "https://175.11.214.29:808",
        "https://118.190.145.138:9001",
        "https://182.112.89.23:8118",
        "https://221.228.17.172:8181",
        "https://115.46.70.48:8123",
        "https://110.88.30.36:808",
        "https://110.87.104.153:8118",
        "https://1.195.25.204:61234",
        "https://119.186.241.31:61234",
        "https://175.155.152.41:61234",
        "https://27.31.103.233:21973",
        "https://125.105.110.4:3128",
        "https://114.222.24.111:808",
        "https://140.250.180.229:61234",
        "https://120.83.98.216:61234",
        "https://175.155.223.179:61234",
        "https://115.198.37.56:6666",
        "https://115.46.74.192:8123",
        "https://106.56.102.39:8070",
        "https://125.121.121.155:6666",
        "https://219.157.147.113:8118",
        "https://117.66.167.57:8118",
        "https://183.128.242.93:6666",
        "https://115.198.39.24:6666",
        "https://114.223.162.171:8118",
        "https://115.46.89.82:8123",
        "https://58.208.16.70:37436",
        "https://123.188.6.176:1133",
        "https://112.195.51.225:61234",
        "https://112.193.131.17:8118",
        "https://221.234.250.204:8010",
        "https://49.79.67.119:61234",
        "https://220.184.215.223:6666",
        "https://180.121.134.176:808",
        "https://122.246.48.118:8010",
        "https://119.7.59.13:61234",
        "https://27.54.248.42:8000",
        "https://59.32.37.99:8010",
        "https://220.191.100.253:6666",
        "https://112.193.70.85:61234",
        "https://60.167.128.91:48963",
        "https://119.4.70.128:61234",
        "https://182.88.166.148:8123",
        "https://113.117.65.112:61234",
        "https://115.226.129.195:61234",
        "https://106.75.71.122:80",
        "https://125.122.171.167:6666",
        "https://125.118.144.247:6666",
        "https://60.184.173.221:8070",
        "https://60.190.250.120:8080",
        "https://36.6.146.199:47025",
        "https://106.56.102.78:808",
        "https://119.7.225.218:61234",
        "https://114.230.69.250:9999",
        "https://111.177.164.2:9999",
        "https://112.85.129.85:9999",
        "https://111.177.176.126:9999",
        "https://1.192.241.146:9999",
        "https://1.198.73.10:9999",
        "https://171.112.165.223:9999",
        "https://125.104.50.54:9999",
        "https://171.112.165.98:9999",
        "https://113.140.1.82:53281",
        "https://221.1.200.242:38652",
        "https://119.102.129.114:9999",
        "https://111.177.182.102:9999",
        "https://116.209.55.227:9999",
        "https://110.52.235.208:9999",
        "https://110.52.235.33:9999",
        "https://112.85.170.221:9999",
        "https://111.77.197.60:808",
        "https://583349285:2zectsyx@139.196.76.78:16816"
    ]
}

lens = len(PROXIES_NEW['https'])
print(lens)
num = 1
while num <= lens:


    try:
        requests.adapters.DEFAULT_RETRIES = 3
        proxies = PROXIES_NEW['https']

        IP = random.choice(proxies)
        # print(IP)
        # print(type(IP))
        b = re.findall('//(\d+\.\d+\.\d+\.\d+):', IP)[0]
        b = b.replace('.', '')
        print(b)
        # thiProxy = "http://" + IP
        # thisIP = "".join(IP.split(":")[0:1])
        # print(thisIP)
        res = requests.get(url="http://icanhazip.com/", timeout=8, proxies={"https": "https://113.140.1.82:53281"})
        proxyIP = res.text
        # print(proxyIP)
        a = proxyIP.replace('.', '')
        print(a)
        if int(a) == int(b):
            print("代理IP:'" + proxyIP + "'有效！")
        else:
            print("返回不是代理池中的ip，代理IP无效！")
    except:
        print("代理IP无效！")
        print(111)
    # else:
    #     print('success')
    num += 1