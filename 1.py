import random

from functools import partial
from timeit import timeit

import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


if __name__ == "__main__":
    array_sizes = [10000, 50000, 100000, 500000]

    deterministic_times = []
    randomized_times = []
    for size in array_sizes:
        arr = [random.randint(-10000, 10000) for _ in range(size)]

        randomized = timeit(partial(randomized_quick_sort, arr.copy()), number=5)
        randomized_times.append(randomized)

        deterministic = timeit(partial(deterministic_quick_sort, arr.copy()), number=5)
        deterministic_times.append(deterministic)

        print(f"Розмір масиву: {size}")
        print(f"    Рандомізований QuickSort: {randomized} секунд")
        print(f"    Детермінований QuickSort: {deterministic} секунд")
        print()

    plt.figure(figsize=(8, 6))
    plt.plot(
        array_sizes, randomized_times, label="Рандомізований QuickSort", color="blue"
    )
    plt.plot(
        array_sizes,
        deterministic_times,
        label="Детермінований QuickSort",
        color="orange",
    )

    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")

    plt.legend()

    plt.show()
