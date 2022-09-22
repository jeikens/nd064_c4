import enum
import requests
import random
import time

def send_something():
    if random.random() < 0.5:
        # FRONTEND
        rand = random.random()
        if rand < 0.05:
            # 5xx
            r = requests.get('http://localhost:8080/500')
        elif rand < 0.1:
            # 4xx
            r = requests.get('http://localhost:8080/not_available')
        else:
            # 2xx
            r = requests.get('http://localhost:8080/')
        print(f'Frontend: {r.status_code}')
    else:
        # BACKEND
        rand = random.random()
        if rand < 0.05:
            # 5xx
            r = requests.get('http://localhost:8080/500')
        elif rand < 0.1:
            # 4xx
            r = requests.get('http://localhost:8080/not_available')
        else:
            # 2xx
            r = requests.get('http://localhost:8081/api')
        print(f'Backend: {r.status_code}')


if __name__ == '__main__':
    while True:
        send_something()
        time.sleep(random.uniform(0,0.2))