class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = "__utmz=51854390.1532780422.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _xsrf=SgZQS6L3lTNIhzeCELXx9ZtVYGrg5M0Z; cap_id=OWFlYzc2ODY4NTg5NDBlYjhhZjllNWEwNGYyY2ZkMjU=|1532785741|879263a789f239a6f95abc78635ebcff0c42a3f2; l_cap_id=NzQyOGUwMWVlNGI0NDNjM2FlOWViYTRjNTQ2NTRmNDU=|1532785741|53718fc4bfac31e66e96995c47e05cba74e092a7; q_c1=0aae74e465ce4dd2b6a3fa4d58c38f10|1532519787000|1532519787000; __utma=51854390.689596102.1532764416.1532778135.1532780422.3; r_cap_id=ZjIyM2NmODdkYmMxNDE1ZmEyMzgwMzZjMTQyMTE0YmI=|1532785741|b4b7968247b54964acc1d631d10dafa3b5a44f32; d_c0=AIAkIbZm9A2PTgYcV52GGXa5SKpBy_abuYs=|1532519787; __utmv=51854390.100--|2=registration_date=20180313=1^3=entry_date=20180313=1; capsion_ticket=2|1:0|10:1532785744|14:capsion_ticket|44:ZGE4MzNiMDFhZGVlNDNkOGE2ZWEwM2VjYTFhYzAzNzc=|5fc05ba6f038d47878bc444bdba3e55554b2433642a09e90386c254d5987278e; _zap=46f0a358-61a3-4ac7-82b9-2fce5bc0bd80; l_n_c=1; n_c=1; z_c0=2|1:0|10:1532785779|4:z_c0|92:Mi4xRlNBdUNBQUFBQUFBZ0NRaHRtYjBEU1lBQUFCZ0FsVk5jOEpKWEFCZEpLRDc2aXYxZk5HSHhQVS1qdTFUZEl0YUp3|200d89b8ec1fcbe903aab70120b24e9dfd9ec67e7f7d197d5c070caa3c2faac8; tgw_l7_route=3072ae0b421aa02514eac064fb2d64b5"
    trans = transCookie(cookie)
    print(trans.stringToDict())