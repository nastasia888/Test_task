import json
import sys


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def fill_values(tests, values):
    value_dict = {item['id']: item['value'] for item in values}

    def recursive_fill(tests):
        for test in tests:
            if test['id'] in value_dict:
                test['value'] = value_dict[test['id']]
            if 'values' in test:
                recursive_fill(test['values'])

    recursive_fill(tests)


def save_report(tests, report_path):
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({'tests': tests}, f, ensure_ascii=False, indent=2)


def main(values_path, tests_path, report_path):
    values = load_json(values_path)['values']
    tests = load_json(tests_path)['tests']

    fill_values(tests, values)

    save_report(tests, report_path)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    main(values_path, tests_path, report_path)
