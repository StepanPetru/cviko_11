import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(numbers):
    numbers = numbers.copy()

    n = len(numbers)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        temp = numbers[i]
        numbers[i] = numbers[min_index]
        numbers[min_index] = temp

    return numbers


def main():
    seznam = [5, 1, 4, 2, 8]
    print("puvodni:", seznam)
    print("serazeny:", selection_sort(seznam))

    nahodny = random_numbers(20)
    print("nahodny:", nahodny)
    print("serazeny nahodny:", selection_sort(nahodny))




if __name__ == "__main__":
    main()















def main():
    print("Hello from cviko-11!")


if __name__ == "__main__":
    main()
