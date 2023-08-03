import asyncio
import httpx
import threading
import time

def sync_main(url,sign):
    response = httpx.get(url).status_code
    print(f'sync_main:{threading.currentThread()}:{sign}:{response}')


sync_start = time.time()
[sync_main(url='https://app.testhtm.com/', sign=i) for i in range(200)]
sync_end = time.time()
print(sync_end - sync_start)