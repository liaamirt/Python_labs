def print_team_positions(teams):
    print("Кількість очок кожної команди:")
    for place, (team, points) in enumerate(teams.items(), start=1):
        print(f"{place}. {team}: {points}")

def add_team(teams, team, points):
    if team in teams:
        print(f"Команда {team} вже є у списку.")
    else:
        teams[team] = points
        print(f"Команда {team} була успішно додана.")

def remove_team(teams, team):
    if team in teams:
        del teams[team]
        print(f"Команда {team} була видалена зі списку.")
    else:
        print(f"Команди {team} немає у списку.")

def find_team_position(teams, team, points):
    sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)
    team_position = sorted_teams.index((team, points)) + 1
    print(f"Команда {team} з {points} очками посідає {team_position}-е місце.")

    lower_teams = [t for t, p in sorted_teams if p < points]
    print("Команди з меншою кількістю очок:")
    for t in lower_teams:
        print(t)

teams = {
    "Team A": 25,
    "Team B": 22,
    "Team C": 18,
    "Team D": 15,
    "Team E": 12,
    "Team F": 10,
    "Team G": 8,
    "Team H": 6,
    "Team I": 3
}

add_team(teams, "Team J", 20)

while True:
    print("\nМеню:")
    print("1. Вивести кількість очок кожної команди")
    print("2. Додати нову команду")
    print("3. Видалити команду")
    print("4. Знайти позицію команди та команди з меншою кількістю очок")
    print("5. Вийти")

    choice = input("Ваш вибір: ")

    if choice == '1':
        print_team_positions(teams)
    elif choice == '2':
        team = input("Введіть назву нової команди: ")
        points = int(input("Введіть кількість очок для цієї команди: "))
        add_team(teams, team, points)
    elif choice == '3':
        team = input("Введіть назву команди, яку потрібно видалити: ")
        remove_team(teams, team)
    elif choice == '4':
        team = input("Введіть назву команди: ")
        points = int(input("Введіть кількість очок: "))
        find_team_position(teams, team, points)
    elif choice == '5':
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")

