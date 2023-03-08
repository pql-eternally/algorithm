"""
Locust 是一个基于 Python 的性能测试工具，可以用来模拟大量用户访问系统，它可以帮助我们快速的了解系统的性能瓶颈，以及系统的最大承载量。
运行命令：
locust -f locustfile.py
"""
from locust import HttpUser, TaskSet, task, between


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": ""
        })

    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/about/")


class WebsiteUser(HttpUser):
    task_set = WebsiteTasks
    wait_time = between(5, 9)
