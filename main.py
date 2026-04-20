import random
import matplotlib.pyplot as plt


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def bubble_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)

    plt.ion()
    plt.show()

    for i in range(n):
        for j in range(0, n - i - 1):

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

            colors = ["steelblue"] * len(numbers)
            colors[j] = "tomato"
            colors[j + 1] = "tomato"

            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

    plt.ioff()
    plt.show()

    return numbers


def main():
    bubble_sort(random_numbers(10))


if __name__ == "__main__":
    main()















def main():
    print("Hello from cviko-11!")


if __name__ == "__main__":
    main()
