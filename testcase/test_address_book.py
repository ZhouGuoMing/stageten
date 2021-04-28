# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : testaddress_book.py
import pytest
import yaml

from address_book.address_book import AddressBook
# 读取加载yaml文件数据
with open(file="test_address_book.yaml") as f:
    datas = yaml.load(f)
    create_number_datas = datas['create_number']
    batch_delete_numbers =datas['batch_delete_numbers']


class TestAddressBook:

    def setup(self):
        self.addressbook=AddressBook()
        self.userid='lisi002'
        self.name='李四'
        self.mobile='13100012313'
        self.department=[1]


    @pytest.mark.parametrize("userid,mobile",
                             list(zip(create_number_datas['userid'],create_number_datas['mobile'])))
    def test_create_number(self,userid,mobile):
        self.addressbook.delete_number(userid)
        r=self.addressbook.create_number(userid, self.name, mobile, self.department)
        assert r.get('errmsg', 'network error') == 'created'
        r=self.addressbook.get_number(userid)
        self.addressbook.delete_number(userid)
        assert r["userid"]== userid

    def test_get_number(self):
        self.addressbook.create_number(self.userid, self.name, self.mobile, self.department)
        r=self.addressbook.get_number(self.userid)
        assert r['errmsg'] == 'ok'
        assert r['name'] == self.name

    def test_update_number(self):
        self.addressbook.delete_number(self.userid)
        self.addressbook.create_number(self.userid, self.name, self.mobile, self.department)
        new_name=self.name+"new"
        r=self.addressbook.update_number(self.userid,self.name,self.department)
        assert r['errmsg'] == 'updated'
        r=self.addressbook.get_number(self.userid)
        assert r['name'] == new_name

    def test_delete_numeber(self):
        self.addressbook.create_number(self.userid,self.name,self.mobile,self.department)
        r=self.addressbook.delete_number(self.userid)
        assert r['errmsg'] == 'deleted'
        r=self.addressbook.get_number(self.userid)
        assert r['errcode'] == 60111

    # 批量删除成员用例
    def test_batch_delete_numbers(self):
        # 先批量创建成员
        for _userid in batch_delete_numbers['userid']:
            for _mobile in batch_delete_numbers['mobile']:
                self.addressbook.create_number(_userid,self.name, _mobile,self.department)
        # 执行批量删除
        r=self.addressbook.batch_delete_numbers(batch_delete_numbers['userid'])
        assert r['errmsg'] == 'deleted'
        for _userid in batch_delete_numbers['userid']:
            r = self.addressbook.get_number(_userid)
        assert r['errcode'] == 60111








