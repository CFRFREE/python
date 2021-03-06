import re
import datetime
import json

from urllib import request
from urllib.parse import quote

keys = ["sqrid", "sqbmid", "rysf",
        "sqrmc", "gh", "sfzh", "sqbmmc", "xb",
        "jgshen", "jgshi", "jgqu", "xhjshen", "xhjshi", "xhjqu",
        "nl", "lxdh", "xjzdz", "xq", "xxss",
        "hcrq", "hccc", "ljqk", "swtw", "xwtw",
        "jkzk", "xrywz", "jtdzshen", "jtdzshi", "jtdzqu", "jtdz",
        "sfyxglz", "yxgcts", "glfs", "zzjc", "tw", "mrxz", "ycqkhb",
        "sfywc", "sfywcdq", "sfywcjtgj", "sfygrzjcg", "sfygrzjcgjtdd",
        "sfyxcgjjc", "sfyxcgjjcgj", "sfyzgfxljs", "sfyzgfxljsjtdd",
        "sfyzgfxryjc", "sfyzgfxryjcdd", "sfyzgfxryjcsj",
        "bz", "fxsj", "yjzt"]


class NoRedirectHandler(request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        return fp

    http_error_301 = http_error_302


class User:
    # properties
    user_agent: str
    user_name: str
    password: str
    data: dict
    # attribute
    opener: request.OpenerDirector
    err_msg: str
    log: str
    # web params
    date: str
    default: str
    route: str
    route_1: str
    jsessionid: str
    jsessionid_1: str
    expires: str
    login_token: str
    sudy_sk: str
    sudy_sk_1: str
    user_pwd: str
    device: str
    groups: str
    username: str
    user_id: str
    uxid: str
    nonce: str
    timestamp: str
    signature: str
    signature2: str
    signature3: str

    def __init__(self, username: str, password: str):
        # 设置当前时间
        now = datetime.datetime.now()
        now_date = now.strftime('%Y-%m-%d')
        now_time = now.strftime('%Y-%m-%d %H:%M')
        # 设置有代理的启动器
        # proxy = request.ProxyHandler({"http": "127.0.0.1:8080"})
        # self.opener = request.build_opener(NoRedirectHandler, proxy)
        # 设置无代理的启动器
        self.opener = request.build_opener(NoRedirectHandler)
        # 设置属性
        self.user_agent = "Mozilla/5.0 (Linux; Android 10; MIX 2S Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 iPortal/25.7"
        self.user_name = username
        self.password = password
        data = {"_ext": "{}", "entity": {"__type": "sdo: com.sudytech.work.suda.jkxxtb.jkxxtb.TSudaJkxxtb"}}
        self.date = now_date
        data['entity']['tbrq'] = now_date
        data['entity']['tjsj'] = now_time
        self.data = data
        self.err_msg = ''
        self.log = ''
        self.default = ''
        self.route_1 = ''

    def req1(self):
        url = 'http://mids.suda.edu.cn/_ids_mobile/login18_9'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': self.user_agent,
            'Accept-Encoding': 'gzip, deflate'
        }
        data = 'password=' + self.password \
               + '&serialNo=0null&username=' + self.user_name
        req = request.Request(url=url, data=bytes(data, 'utf-8'), headers=headers, method='POST')
        result = self.opener.open(req)
        t = re.split(pattern=r'[=; ,{}:"]+', string=result.getheader("set-cookie"))
        t1 = re.split(pattern=r'[=; ,{}:"]+', string=result.getheader("ssoCookie"))
        self.route = t[t.index('route') + 1]
        self.jsessionid = t[t.index('JSESSIONID') + 1]
        self.expires = t[t.index('Expires') + 1]
        self.login_token = t[t.index('LOGIN_TOKEN') + 1]
        self.sudy_sk = t1[t1.index('sudy_sk') + 6]
        self.user_pwd = result.getheader("userPwd")

    def req2(self):
        url = 'http://mids.suda.edu.cn/_ids_mobile/loginedUser15'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': self.user_agent,
            'Cookie': 'route=' + self.route + '; '
                      + 'JSESSIONID=' + self.jsessionid + '; {'
                      + '"Expires":' + self.expires + '=; '
                      + '"LOGIN_TOKEN":"' + self.login_token + '"=; '
                      + '"Max-Age":7200=; "Path":"/sso"}=; '
                      + 'sudy_sk=' + self.sudy_sk + '; '
                      + 'LOGIN_TOKEN=' + self.login_token,
            'Cookie2': '$Version=1',
            'Accept-Encoding': 'gzip, deflate'
        }
        req = request.Request(url=url, data=None, headers=headers, method='POST')
        result = self.opener.open(req)
        t = re.split(pattern=r'[=; ,{}:"]+', string=result.getheader("set-cookie"))
        self.sudy_sk_1 = t[t.index('sudy_sk') + 1]
        read_result = result.read()  # 这个操作会改变result，无法再次读取
        json_object = json.loads(read_result.decode('utf-8'))
        self.device = json_object['data']['device']
        self.groups = json_object['data']['groups']
        self.username = json_object['data']['username']
        self.user_id = json_object['data']['userId']
        self.uxid = json_object['data']['uxid']

    def req3(self):
        url = 'http://aff.suda.edu.cn/mobile/updateUserAppList_21.mo'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': self.user_agent,
            'Cookie': 'LOGIN_TOKEN=' + self.login_token + '; '
                      + 'sudy_sk=' + self.sudy_sk_1
        }
        data = 'appIds=2750'
        req = request.Request(url=url, data=bytes(data, 'utf-8'), headers=headers, method='POST')
        result = self.opener.open(req)
        t = re.split(pattern=r'[=; ,{}:"]+', string=result.getheader("set-cookie"))
        self.jsessionid_1 = t[t.index('JSESSIONID') + 1]

    def req4(self):
        url = 'http://aff.suda.edu.cn/mobile/openApp20.mo'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': self.user_agent,
            'Cookie': 'LOGIN_TOKEN=' + self.login_token + '; '
                      + 'sudy_sk=' + self.sudy_sk_1 + '; '
                      + 'JSESSIONID=' + self.jsessionid_1
                      + '; HttpOnly=; Secure=',
            'Cookie2': '$Version=1',
            'Accept-Encoding': 'gzip, deflate'
        }
        data = 'uxid=' + self.uxid + '&id=2750&userId=' + self.user_id \
               + '&device=' + self.device + '&group=' + '%2C'.join(self.groups.split(',')) + '&isSign=1'
        req = request.Request(url=url, data=bytes(data, 'utf-8'), headers=headers, method='POST')
        result = self.opener.open(req)
        # read_result = zlib.decompress(result.read(), zlib.MAX_WBITS | 16)  # 不通过burpsuite的读取方式
        read_result = result.read()  # 这个操作会改变result，无法再次读取  # 通过burpsuite的读取方式
        json_object = json.loads(read_result.decode('utf-8'))
        self.timestamp = json_object['data']['iportal.timestamp']
        self.nonce = json_object['data']['iportal.nonce']
        self.signature = json_object['data']['iportal.signature']
        self.signature2 = json_object['data']['iportal.signature2']
        self.signature3 = json_object['data']['iportal.signature3']

    def req5(self):
        url = 'http://dk.suda.edu.cn/default/work/suda/jkxxtb/index.jsp?f=app'
        params = {
            'iportal.timestamp': self.timestamp,
            'iportal.nonce': self.nonce,
            'iportal.signature': self.signature,
            'iportal.signature2': self.signature2,
            'iportal.signature3': self.signature3,
            'iportal.device': self.device,
            'iportal.group': '%2C'.join(self.groups.split(',')),
            'iportal.uid': self.user_id,
            'iportal.uname': quote(self.username, encoding='GBK'),
            'iportal.uxid': self.uxid
        }
        for key, value in params.items():
            url = url + '&' + key + '=' + value
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;\
            q=0.8,application/signed-exchange;v=b3;q=0.9',
            'X-Requested-With': 'com.wisorg.szdx',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': 'sudy_sk=' + self.sudy_sk + '; LOGIN_TOKEN=' + self.login_token
        }
        req = request.Request(url=url, data=None, headers=headers, method='GET')
        result = self.opener.open(req)
        t = re.split(pattern=r'[=; ,{}:"]+', string=result.getheader("set-cookie"))
        self.default = t[t.index('default') + 1]
        self.route_1 = t[t.index('route') + 1]

    def req6(self):
        url = 'http://dk.suda.edu.cn/default/work/suda/jkxxtb/' \
              'com.sudytech.portalone.base.db.queryBySqlWithoutPagecond.biz.ext'
        headers = {
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': self.user_agent,
            'Content-Type': 'text/json',
            'Origin': 'http://dk.suda.edu.cn',
            'Referer': 'http://dk.suda.edu.cn/default/work/suda/jkxxtb/jkxxcj.jsp',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': 'default=' + self.default + '; '
                      + 'route=' + self.route_1 + '; '
                      + 'sudy_sk=' + self.sudy_sk + '; '
                      + 'LOGIN_TOKEN=' + self.login_token
        }
        data = '{"params":{"empcode":"' + self.user_name + '"},' \
               + '"querySqlId":"com.sudytech.work.suda.jkxxtb.jkxxtb.queryNear"}'
        req = request.Request(url=url, data=bytes(data, encoding='utf-8'), headers=headers, method='POST')
        result = self.opener.open(req)
        read_result = result.read()
        t = re.split(pattern=r'[=; ,{}:"]+', string=read_result.decode('utf-8'))
        for key in keys:
            self.data['entity'][key] = t[t.index(key.upper()) + 1]
        tbrq = t[t.index('TBRQ') + 1]
        if tbrq == self.date:
            self.data['entity']['id'] = int(t[t.index('ID') + 1])

    def req7(self) -> int:
        url = 'http://dk.suda.edu.cn/default/work/suda/jkxxtb/com.sudytech.portalone.base.db.saveOrUpdate.biz.ext'
        headers = {
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': self.user_agent,
            'Content-Type': 'text/json',
            'Origin': 'http://dk.suda.edu.cn',
            'Referer': 'http://dk.suda.edu.cn/default/work/suda/jkxxtb/jkxxcj.jsp',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': 'default=' + self.default + '; '
                      + 'route=' + self.route_1 + '; '
                      + 'LOGIN_TOKEN=' + self.login_token + '; '
                      + 'sudy_sk=' + self.sudy_sk
        }
        req = request.Request(
            url=url,
            data=bytes(json.dumps(self.data), encoding='utf-8'),
            headers=headers,
            method='POST'
        )
        result = self.opener.open(req)
        code = result.getcode()
        if code != 200:
            self.err_msg += str(code)
            return -1
        content_dict = json.loads(result.read().decode('utf-8'))
        if content_dict.get('result') is None:
            self.err_msg += json.dumps(content_dict.get('exception'))
            return -2
        self.log += content_dict['resultEntity']['gh'] + '  ' \
            + str(content_dict['resultEntity']['id']) + '  ' \
            + '填表日期="' + content_dict['resultEntity']['tbrq'] + '"  ' \
            + '提交时间="' + content_dict['resultEntity']['tjsj'] + '"'
        return 0

    def logging(self):
        f = open('DaKa.log', 'a', encoding='utf-8')
        content = self.log if self.err_msg == '' else self.err_msg
        f.write(content + '\n')
        f.close()

    def get_err_msg(self) -> str:
        return self.err_msg

    def check_up(self) -> int:
        fun_list = [self.req1, self.req2, self.req3, self.req4, self.req5, self.req6, self.req7, self.logging]
        result = 0
        c = 0
        for fun in fun_list:
            if c == 6:
                result = fun()
            else:
                fun()
            print('.', end='')
            c += 1
        return result


if __name__ == '__main__':
    username= '2002406017'
    password = 'Free221818'
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + f'  {username}: ', end='')
    u = User(username, password)
    result = u.check_up()
    if result != 0:
        print(' failed.')
    else:
        print(' finished!')
