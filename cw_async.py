import threading
import time
from queue import Queue

# class FileWorker(threading.Thread):
#     def __init__(self, name, queue):
#         super().__init__()
#         self.name = name
#         self.queue = queue
#
#     def run(self):
#         time.sleep(0.1)
#         results = len(self.name)
#         self.queue.put((self.name, results))
#
#
# result = {}
# threads = []
#
# files = ['qwerty', 'asd', 'gamma', 'python']
# queue = Queue()
#
# for f in files:
#     t = FileWorker(f, queue)
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# while not queue.empty():
#     key, vale = queue.get()
#     result[key] = vale
#
# print(result)
#
# counter = 0
#
#
# def increment():
#     global counter
#     for i in range(10000):
#         counter += 1
#
#
# threads = [threading.Thread(target=increment),
#            threading.Thread(target=increment),
#            threading.Thread(target=increment)]
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()
#
# print(counter)
import asyncio
import random


async def task(name):
    print(f"{name} start")
    await asyncio.sleep(2)
    print(f"{name} finish")


async def hello(name):
    print(f"{name} start")
    delay = random.randint(1, 3)
    await asyncio.sleep(delay)
    print(f"Hello, {name}, wait {delay}")


import requests
import aiohttp

urls = ['https://itstep.dp.ua/', "https://itstep.us/", 'https://itstep.dp.ua/', "https://itstep.us/",
        'https://itstep.dp.ua/', "https://itstep.us/"] * 5
start = time.time()
for url in urls:
    r = requests.get(url)
    print(f"get {len(r.text)} symbols")
    # print(r.text)
print("time: ", time.time() - start)


async def getUrl(session, url):
    async with session.get(url) as resp:
        text = await resp.text()
        print(f"get {len(text)} symbols")
        return text


async def main():
    # names = ['Bill', 'Bob', 'Nick']
    # tasks = [hello(n) for n in names]
    # await asyncio.gather(*tasks)
    global urls
    async with aiohttp.ClientSession() as session:
        tasks = [getUrl(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print("time: ", time.time() - start)
