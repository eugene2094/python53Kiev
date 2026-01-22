import time, random
import threading


class ApiClient:
    def fetch_user(self, user_id):
        print(f"Request user {user_id}")
        timer = random.uniform(1, 2)
        print(timer)
        time.sleep(timer)
        return {'id': user_id, "name": f"User {user_id}"}


class UserService:
    def __init__(self):
        self.client = ApiClient()

    def load_users(self, user_ids):
        users = []
        for uid in user_ids:
            users.append(self.client.fetch_user(uid))
        return users


class UserLoader(threading.Thread):
    def __init__(self, user_id, client, results):
        super().__init__()
        self.user_id = user_id
        self.client = client
        self.results = results

    def run(self):
        user = self.client.fetch_user(self.user_id)
        self.results.append(user)


class UserServiceThread:
    def __init__(self):
        self.client = ApiClient()

    def load_users_parallel(self, user_ids):
        threads = []
        results = []

        for uid in user_ids:
            t = UserLoader(uid, self.client, results)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        return results


# start = time.time()
# service = UserService()
# service.load_users([1, 2, 3, 4, 5])
# print(time.time() - start)
#
# start = time.time()
# service = UserServiceThread()
# service.load_users_parallel([1, 2, 3, 4, 5])
# print(time.time() - start)


def heavy():
    s = 0
    for i in range(100000000):
        s += 1
    return s


# print(heavy())
# print(heavy())

from multiprocessing import Process


def task(name):
    print(f"start {name}")
    heavy()
    print(f"end {name}")


class Worker(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        heavy()


if __name__ == "__main__":
    p1 = Process(target=task, args=('a',))
    p2 = Process(target=task, args=('b',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
