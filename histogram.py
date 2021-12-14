import concurrent.futures
import random
import matplotlib.pyplot as plt
from collections import Counter


def get_random_number():
    return random.randint(1, 1000)

def calculate_histogram(nb_of_numbers):
    numbers = [get_random_number() for _ in range(nb_of_numbers)]
    histogram = Counter(numbers)
    return histogram


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as thread:
        th = thread.submit(calculate_histogram, 1000000)
        histogram = th.result()
        plt.bar(histogram.keys(), histogram.values())
        plt.show()