import csv

def read_csv(file_path):
    data = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка при зчитуванні файлу '{file_path}': {e}")
        return None

def write_csv(data, file_path):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data)
        print(f"Дані було успішно записано у файл '{file_path}'.")
    except Exception as e:
        print(f"Виникла помилка при записі у файл '{file_path}': {e}")

def main():
    input_file = 'dataBase.csv'
    output_file = 'output.csv'

    data = read_csv(input_file)
    if data is None:
        return
    
    print("Вміст CSV файлу:")
    for row in data:
        print(row)

    countries = input("Введіть назви країн через кому (наприклад, Ukraine, Germany): ").split(',')

    filtered_data = []
    for row in data:
        if row[2] in countries:
            filtered_data.append(row)

    write_csv(filtered_data, output_file)

if __name__ == "__main__":
    main()

