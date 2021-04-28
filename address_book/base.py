# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : base.py
import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params={"access_token":self.token}

    def get_token(self):
        r=requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='
                       'ww65766ff6db64205d&corpsecret=nC_218vYvuzeQQ_DlrJ-_zik9NQI_FVJblR4k8RW-Lo')
        token=r.json()['access_token']
        return token
