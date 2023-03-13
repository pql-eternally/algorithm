"""
Locust 是一个基于 Python 的性能测试工具，可以用来模拟大量用户访问系统，它可以帮助我们快速的了解系统的性能瓶颈，以及系统的最大承载量。
运行命令：
locust -f locust_demo.py

locust -u 200 -r 20 -t 1m -f locust_demo.py
-u: 指定总用户数
-r: 指定每秒启动用户数
-t: 指定运行时间（格式：1m，1h）
-f: 指定脚本文件

flask api test: locust --host=http://localhost:5000 -u 200 -r 20 -t 1m -f locust_demo.py
fastapi api test: locust --host=http://localhost:8000  -u 200 -r 20 -t 1m -f locust_demo.py
"""
from locust import HttpUser, TaskSet, task, between


class WebsiteTasks(TaskSet):
    def on_start(self):
        pass

    @task
    def index(self):
        self.client.get("/")

    @task
    def sleep(self):
        self.client.get("/sleep")


class WebsiteUser(HttpUser):
    wait_time = between(5, 9)
    # flask host
    # host = "http://127.0.0.1:5000"
    tasks = [WebsiteTasks]
