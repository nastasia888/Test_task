import sys


def circular_array_path(n, m):
    # Создаем круговой массив от 1 до n
    circular_array = list(range(1, n + 1))
    path = []

    # Начальная позиция
    current_index = 0

    # Цикл для получения интервалов
    while True:
        # Добавляем текущий элемент в путь
        path.append(circular_array[current_index])

        # Находим следующий индекс, с учетом длины m
        current_index = (current_index + m) % n

        # Если вернулись на первый элемент, прерываем цикл
        if current_index == 0:
            break

    return ''.join(map(str, path))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py <n> <m>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    result = circular_array_path(n, m)
    print(result)
