def bubble_sort(data):
    count = 0
    for num in data:
        count += 1

    for i in range(count):
        for j in range(0, count - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def bubble_sort_half(data):
    count = 0
    for num in data:
        count += 1

    half = count // 2
    for i in range(half):
        for j in range(0, half - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def find_largest(numbers, k):
    count = 0
    for num in numbers:
        count += 1

    if count < k or k <= 0:
        return "Некоректне значення k", -1

    sorted_numbers = []
    for num in numbers:
        sorted_numbers.append(num)

    bubble_sort(sorted_numbers)
    largest_value = sorted_numbers[-k]

    index = -1
    for i in range(count):
        if numbers[i] == largest_value:
            index = i
            break

    return largest_value, index


def find_largest_half(numbers, n):
    count = 0
    for num in numbers:
        count += 1

    half = count // 2
    if half < n or n <= 0:
        return "Некоректне значення n", -1

    half_numbers = []
    for i in range(half):
        half_numbers.append(numbers[i])

    sorted_half = []
    for num in half_numbers:
        sorted_half.append(num)

    bubble_sort_half(sorted_half)
    largest_value = sorted_half[-n]

    index = -1
    for i in range(half):
        if numbers[i] == largest_value:
            index = i
            break

    return largest_value, index


data = [15, 7, 22, 9, 36, 2, 42, 18]
print("Масив:", data)

k = int(input("Введіть значення k: "))
value, index = find_largest(data, k)
if index == -1:
    print("Некоректне значення k")
else:
    print(f"Знайдений {k}-й найбільший елемент: {value}")
    print(f"Позиція {k}-го найбільшого елемента: {index}")

n = int(input("Введіть значення n: "))
value, index = find_largest_half(data, n)
if index == -1:
    print("Некоректне значення n")
else:
    print(f"Знайдений {n}-й найбільший елемент у першій половині: {value}")
    print(f"Позиція {n}-го найбільшого елемента в першій половині: {index}")