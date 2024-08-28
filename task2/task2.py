import sys


def read_circle_data(filename):
    with open(filename, 'r') as file:
        x, y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return (x, y, radius)


def read_points_data(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            points.append(tuple(map(float, line.strip().split())))
    return points


def point_position(circle, point):
    cx, cy, radius = circle
    px, py = point
    distance_squared = (px - cx) ** 2 + (py - cy) ** 2
    radius_squared = radius ** 2

    if distance_squared < radius_squared:
        return 1  # точка внутри
    elif distance_squared == radius_squared:
        return 0  # точка на окружности
    else:
        return 2  # точка снаружи


def main(circle_file, points_file):
    circle = read_circle_data(circle_file)
    points = read_points_data(points_file)

    for point in points:
        position = point_position(circle, point)
        print(position)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Использование: python task2.py circle_file.txt points_file.txt")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    main(circle_file, points_file)
