def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
    except FileNotFoundError:
        print("Файл", file_name, "не знайдено!")
        return None
    except:
        print("Помилка відкриття файлу", file_name)
        return None
    else:
        print("Файл", file_name, "був відкритий успішно!")
        return file

def create_tf1_1(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("Hello world!\n")
            file.write("This is a test sentence.\n")
            file.write("Python programming is fun!\n")
            file.write("We are learning file handling.\n")
            file.write("This file has different length strings.\n")
        print(f"Файл {file_name} був успішно створений.")
    except Exception as e:
        print(f"Виникла помилка при створенні файлу: {e}")

def process_tf1_1_to_tf1_2(input_file_name, output_file_name):
    input_file = open_file(input_file_name, "r")
    output_file = open_file(output_file_name, "w")

    if input_file and output_file:
        try:
            for line in input_file:
                words = line.split()
                for word in words:
                    output_file.write(word + '\n')
            print(f"Файл {output_file_name} був успішно записаний з вмісту {input_file_name}.")
        except Exception as e:
            print(f"Виникла помилка при обробці файлів: {e}")
        finally:
            input_file.close()
            output_file.close()

def print_file_content(file_name):
    file = open_file(file_name, "r")
    if file:
        print(f"Вміст файлу {file_name}:")
        for line in file:
            print(line.strip())
        file.close()
        print(f"Файл {file_name} був успішно закритий.")

tf1_1_file = "TF1_1.txt"
tf1_2_file = "TF1_2.txt"

create_tf1_1(tf1_1_file)

process_tf1_1_to_tf1_2(tf1_1_file, tf1_2_file)

print_file_content(tf1_2_file)
