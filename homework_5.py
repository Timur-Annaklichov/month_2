from datetime import datetime

def checktime(func):
    def wrapper(*args, **kwargs):
        time_now = datetime.now()
        print(f"функция была вызвана в {time_now.hour}:{time_now.minute}:{time_now.second} {time_now.day}/{time_now.month}/{time_now.year}")
        func(*args, **kwargs)
    return wrapper

@checktime
def hello_world(name):
    print(f"hello world from {name}")

hello_world('Timur')
