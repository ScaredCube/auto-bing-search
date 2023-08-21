import requests,random,time

#搜索次数
n=30

#账号
accs=[
    'username1@outlook.com',
    'username2@outlook.com'
]


with open('cookies.txt','r',encoding='utf-8') as f:
    cookies=f.read().split('\n')


headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

def cookie_dict(coo):
    cookie = {i.split("=")[0]:i.split("=")[1] for i in coo.split(";")}
    return cookie


def sou(search, c):
    global headers
    url=f'https://cn.bing.com/search?q={search}'
    result=requests.get(url,headers=headers, cookies=cookie_dict(c)).text
    #print(result)

def sous(cookie):
    with open('THUOCL_it.txt','r',encoding='utf-8') as f:
        content=f.read().split('\n')
    for i in range(1,n+1):
        c=random.choice(content).split('\t')[0]
        print(f'正在搜索{c}({i}/{n})')
        sou(c,cookie)
        time.sleep(0.5)

def isLogin(coo,acc):
    global headers
    url='https://cn.bing.com/'
    try:
        result=requests.get(url,headers=headers, cookies=cookie_dict(coo)).text
    except:
        print(print(f'-----{acc}登录失败！请检查cookie设置-----'))
        return False
    if acc in str(result):
        #print(f'{acc}登录成功')
        return True
    else:
        print(print(f'-----{acc}登录失败！请检查cookie设置-----'))
        return False


#----main----

for i in range(len(accs)):
    if isLogin(cookies[i],accs[i]):
        print(f'-----{accs[i]}登录成功-----')
        sous(cookies[i])

