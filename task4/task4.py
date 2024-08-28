import sys


def min_moves_to_equal_array(nums):
    average = sum(nums) // len(nums)
    moves = sum(abs(num - average) for num in nums)
    return moves


def main():
    if len(sys.argv) != 2:
        print("Использование: python task4.py numbers.txt")
        return

    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            nums = [int(line.strip()) for line in file]

        result = min_moves_to_equal_array(nums)
        print(result)

    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
    except ValueError:
        print("Ошибка: файл должен содержать только целые числа.")


if __name__ == "__main__":
    main()
