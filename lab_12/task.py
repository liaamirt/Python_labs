import json
import os

def read_json_objects(filename):
    with open(filename, "r") as file:
        objects = json.load(file)
    return objects

def write_json_objects(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def print_json_content(filename):
    try:
        data = read_json_objects(filename)
        print(f"Зміст JSON файлу '{filename}':")
        for obj in data:
            print(obj)
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")

def add_new_record(filename):
    try:
        data = read_json_objects(filename)
    except FileNotFoundError:
        data = []
    
    new_record = {
        "TeamName": input("Введіть назву нової команди: "),
        "Score": int(input("Введіть кількість очок, які набрала команда: "))
    }
    
    data.append(new_record)
    write_json_objects(filename, data)
    print(f"Новий запис додано до JSON файлу '{filename}'.")

def delete_record_by_teamname(filename):
    try:
        data = read_json_objects(filename)
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return
    
    team_name = input("Введіть назву команди для видалення: ")
    updated_data = [obj for obj in data if obj["TeamName"] != team_name]
    
    if len(updated_data) < len(data):
        write_json_objects(filename, updated_data)
        print(f"Запис з назвою '{team_name}' видалено з JSON файлу '{filename}'.")
    else:
        print(f"Команда з назвою '{team_name}' не знайдена у JSON файлі.")

def search_by_teamname(filename):
    try:
        data = read_json_objects(filename)
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return
    
    team_name = input("Введіть назву команди для пошуку: ")
    found_teams = [obj for obj in data if obj["TeamName"].lower() == team_name.lower()]
    
    if found_teams:
        print(f"Знайдені записи для команди '{team_name}':")
        for team in found_teams:
            print(team)
    else:
        print(f"Команда з назвою '{team_name}' не знайдена у JSON файлі.")

def solve_task(filename, new_team_name, new_team_score):
    try:
        data = read_json_objects(filename)
    except FileNotFoundError:
        data = []
    
    scores = [obj["Score"] for obj in data]
    place, lesser_teams = find_team_place(scores, new_team_score)
    
    new_team_record = {
        "TeamName": new_team_name,
        "Score": new_team_score,
        "Place": place
    }
    
    data.append(new_team_record)
    write_json_objects(filename, data)
    
    print(f"Задачу вирішено. Результати записані в JSON файл '{filename}'.")
    print(f"Нова команда '{new_team_name}' з набраними {new_team_score} очками зайняла {place}-е місце.")
    print(f"Команди, які набрали менше очок, ніж '{new_team_name}':")
    for i, team_score in enumerate(lesser_teams, start=1):
        print(f"{i}. Очки: {team_score}")

def find_team_place(scores, new_team_score):
    n = len(scores) + 1  
    teams = sorted(scores, reverse=True)  

    new_team_place = 1
    for score in teams:
        if new_team_score < score:
            new_team_place += 1
        else:
            break

    lesser_teams = [team_score for team_score in teams if team_score < new_team_score]
    
    return new_team_place, lesser_teams

def main():
    json_filename = "football_teams.json"

    while True:
        print("\nОберіть операцію:")
        print("1. Виведення на екран вмісту JSON файлу")
        print("2. Додавання нового запису у JSON файл")
        print("3. Видалення запису з JSON файлу за назвою команди")
        print("4. Пошук даних у JSON файлі за назвою команди")
        print("5. Розв’язання завдання (додавання нової команди та виведення результатів)")
        print("6. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            print_json_content(json_filename)

        elif choice == '2':
            add_new_record(json_filename)

        elif choice == '3':
            delete_record_by_teamname(json_filename)

        elif choice == '4':
            search_by_teamname(json_filename)

        elif choice == '5':
            new_team_name = input("Введіть назву нової команди: ")
            new_team_score = int(input("Введіть кількість очок, які набрала ця команда: "))
            solve_task(json_filename, new_team_name, new_team_score)

        elif choice == '6':
            print("До побачення!")
            break

        else:
            print("Неправильний вибір. Будь ласка, виберіть ще раз.")

if __name__ == "__main__":
    main()
