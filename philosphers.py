import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, name, leftFork, rightFork):
        threading.Thread.__init__(self)
        self.name = name
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run(self):
        while True:
            print("{} is thinking".format(self.name))
            time.sleep(random.uniform(1, 10))
            print("{} is hungry".format(self.name))
            self.dine()

    def dine(self):
        self.leftFork.acquire()
        self.rightFork.acquire()

        print("{} is eating".format(self.name))
        time.sleep(random.uniform(1, 10))

        self.leftFork.release()
        self.rightFork.release()

if __name__ == "__main__":
    forks = [threading.Lock() for n in range(5)]
    philosophers = [Philosopher(name="P{}".format(n),
                                leftFork=forks[n % 5],
                                rightFork=forks[(n + 1) % 5]) for n in range(5)]
    for p in philosophers:
        p.start()