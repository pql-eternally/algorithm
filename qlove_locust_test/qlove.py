"""
Locust 是一个基于 Python 的性能测试工具，可以用来模拟大量用户访问系统，它可以帮助我们快速的了解系统的性能瓶颈，以及系统的最大承载量。
运行命令：
locust -f locust_demo.py

locust -u 200 -r 20 -t 1m -f locust_demo.py
-u: 指定总用户数
-r: 指定每秒启动用户数
-t: 指定运行时间（格式：1m，1h）
-f: 指定脚本文件

flask api test: locust --host=http://127.0.0.1:5000 -u 200 -r 20 -t 1m -f locust_demo.py
fastapi api test: locust --host=http://127.0.0.1:8000  -u 200 -r 20 -t 1m -f locust_demo.py
"""
from locust import HttpUser, TaskSet, task, between
from qcore.api.client import ApiClient
from mongodb.bootstrap import bootstrap_mongo

bootstrap_mongo()

from qcore.core.globals import db

app_config = {
    'http_gw': 'http://127.0.0.1:8081',
    'access_key': '63ae4f6d51ad6324727f25e1',
    'secret_key': '63ae4f6d51ad6324727f25e2',
    'test_phone': '13800138000',
    'test_code': '6666',
}


class WebsiteTasks(TaskSet):

    def on_start(self):
        pass

    @property
    def x_auth_client(self):
        client = ApiClient(
            access_key=app_config['access_key'],
            secret_key=app_config['secret_key'],
            api_gateway=app_config['http_gw'],
            namespace='qlove',
            api_version='1.0'
        )
        return client

    def x_token_client(self):
        access_key = app_config['access_key']
        secret_key = app_config['secret_key']
        app_record = db.AppKey.find_one({'access_key': access_key, 'secret_key': secret_key})
        assert app_record, 'App not found.'
        app_id = app_record['app_id']

        # fetch account
        phone = app_config['test_phone']
        verify_code = app_config['test_code']
        account_record = db.Account.find_one({'phone': phone, 'state': 100})
        assert account_record, f'Account[{phone}] not found.'

        account_id = account_record['_id']
        # fetch access token
        record = db.AccessToken.find_one_by_sort({'app_id': app_id, 'account_id': account_id}, [('created_at', -1)])
        if record and record.is_ok:
            access_token = record['_id']
        else:
            # login to get access token
            params = {
                "phone": phone,
                "verify_code": verify_code,
            }
            try:
                service = self.x_auth_client.get_api_module('auth.auth')
                result = service.login(**params)
                access_token = result.get('access_token')
                assert access_token, 'Login failed.'
            except Exception as e:
                print(e)
                raise e

        client = ApiClient(
            access_key=access_key,
            secret_key=secret_key,
            access_token=access_token,
            api_gateway=app_config['http_gw'],
            namespace='qlove',
            api_version='1.0'
        )
        return client

    @task
    def sleep(self):
        self.client.get("/sleep")


class WebsiteUser(HttpUser):
    wait_time = between(5, 10)
    tasks = [WebsiteTasks]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

