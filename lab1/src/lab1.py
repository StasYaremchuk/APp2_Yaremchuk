def bubble_sort(data):
    count = 0
    for num in data:
        count += 1

    for i in range(count):
        for j in range(0, count - i - 1):
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


data = [15, 7, 22, 9, 36, 2, 42, 18]
print("Масив:", data)

k = int(input("Введіть значення k: "))

value, index = find_largest(data, k)
if index == -1:
    print("Некоректне значення k")
else:
    print(f"Знайдений {k} найбільший елемент: {value}")
    print(f"Позиція {k} найбільшого елемента: {index}")
