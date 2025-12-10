'''from locust import HttpUser, task

class LocustWebUserTest(HttpUser):
    host = "http://127.0.0.1:8080"
    @task
    def hello_world(self):
        self.client.get("/index.html")
    @task(3)
    def hello_worlk(self):
        self.client.get("/")
    @task(2)
    def hello_worl(self):
        self.client.get('/user/<name>.html')

'''
    
