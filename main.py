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


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, value):
        indexes = []

        for i in range(len(self.scores)):
            if self.scores[i] == value:
                indexes.append(i)

        return indexes

    def get_sorted(self):
        scores = self.scores.copy()
        n = len(scores)

        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print("count:", results.count())

    for i in range(results.count()):
        print("Student", i, ":", results.get_by_index(i), "-", results.get_grade(i))

    print("find 100:", results.find(100))
    print("find 50:", results.find(50))
    print("find 77:", results.find(77))

    print("sorted:", results.get_sorted())

    print("bubble animation:")
    bubble_sort(random_numbers(10))


if __name__ == "__main__":
    main()