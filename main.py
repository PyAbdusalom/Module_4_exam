import threading
from datetime import timedelta

import httpx
import redis


def thread(name):
    connection = redis.Redis(host="localhost", port=6379, decode_responses=True)
    response = httpx.get(f"https://{name}")
    data = response.content
    connection.set(name=name, value=data, ex=timedelta(60))


oqim1 = threading.Thread(target=thread, args=('kun.uz',))
oqim2 = threading.Thread(target=thread, args=("daryo.uz",))
oqim3 = threading.Thread(target=thread, args=("qalampir.uz",))
oqim4 = threading.Thread(target=thread, args=("leetcode.com",))
oqim5 = threading.Thread(target=thread, args=("atto.uz/uz",))

oqim1.start()
oqim2.start()
oqim3.start()
oqim4.start()
oqim5.start()

oqim1.join()
oqim2.join()
oqim3.join()
oqim4.join()
oqim5.join()


