# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : address_book.py

from address_book.base import Base


class AddressBook(Base):

    def create_number(self, userid, name, mobile,department):
        create_number_url='https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data={
            "userid":userid,
            "name":name,
            "mobile":mobile,
            "department":department
        }
        r=self.s.post(url=create_number_url, json=data)
        return r.json()

    def get_number(self, userid):
        get_number_url='https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params={
            'userid':userid
        }
        r=self.s.get(url=get_number_url, params=params)
        return r.json()

    def update_number(self, userid, name, department):
        update_number_url='https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data={
            'uesrid':userid,
            'name':name,
            'department':department
        }
        r=self.s.post(url=update_number_url, json=data,)
        return r.json()

    def delete_number(self, userid):
        dalete_number_url='https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params={
            'userid':userid
        }
        r=self.s.get(url=dalete_number_url, params=params)
        return r.json()

    def batch_delete_numbers(self,useridlist:list):
        batch_delete_numbers_url='https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?debug=1'
        data={
            'useridlist':useridlist
        }
        r=self.s.post(batch_delete_numbers_url,json=data)
        return r.json()