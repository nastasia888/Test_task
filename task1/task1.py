import sys


def circular_array_path(n, m):
    array = list(range(1, n + 1))
    path = []
    current_index = 0

    while True:
        path.append(array[current_index])
        current_index = (current_index + m - 1) % n

        if current_index == 0:
            break

    return ''.join(map(str, path))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python task1.py n m")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    result = circular_array_path(n, m)
    print(result)
