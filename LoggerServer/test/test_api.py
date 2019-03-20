from unittest import TestCase
import requests
from requests import Response,Request

class TeatLogger(TestCase):
    def test_query(self):
        url='http://localhost:5000/'
        #method=get
        resp:Response=requests.get(url)
        self.assertEqual(resp.status_code,200)
            #print(resp.headers.get('Content-Type'))
        try:
            self.assertEqual(resp.headers.get('Content-Type'),'applition/json')
        except:
            print(123)
        data=resp.json()
        self.assertEqual(data.get('code'),10001)
    def test_upload(self):
        url='http://10.35.366.17:5000/upload_log/'
        digit=open('download.png','rb')
        data={
            'msg':'日志',
            'name':'flask-looger',

        }
        files={

            'digit_0':digit,
        }

        #上传json数据
        # data=表单数据
        # json=json数据
        #files和json都是字节流，不能同时上传
        resp=requests.post(url,json=data,files=files)
        self.assertEqual(resp.status_code,200)

        result=resp.json() #获取响应的json
        self.assertIsNone(result,'响应的数据不是json格式')
        self.assertEqual(result.get('code'),7000)
