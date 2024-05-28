import pandas as pd

students = {
    "Vitaly_Prikhodko": {"first_name": "Віталій", "last_name": "Приходько", "middle_name": "Миколайович", "birthdate": (2004, 25, 10), "grades": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10]},
    "Dmytro_Kropyvnytskyi": {"first_name": "Дмитро", "last_name": "Кропивницький", "middle_name": "Андрійович", "birthdate": (2003, 5, 12), "grades": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4]},
    "Mikhail_Romanenko": {"first_name": "Михайло", "last_name": "Романенко", "middle_name": "Ігорович", "birthdate": (2005, 11, 5), "grades": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4]},
    "Maxim_Derizemlya": {"first_name": "Максим", "last_name": "Деріземля", "middle_name": "Олександрович", "birthdate": (2002, 8, 7), "grades": [12, 4, 10, 7, 5, 8, 3, 3, 5, 7]},
    "Victoria_Zhuk": {"first_name": "Вікторія", "last_name": "Жук", "middle_name": "Олександрівна", "birthdate": (2006, 4, 3), "grades": [10, 10, 10, 9, 10, 9, 10, 8, 7, 12]},
    "Andrey_Kuryanov": {"first_name": "Андрій", "last_name": "Кур'янов", "middle_name": "Юрійович", "birthdate": (2005, 8, 7), "grades": [5, 6, 7, 5, 4, 7, 5, 4, 4, 8]},
    "Oksana_Dubovets": {"first_name": "Оксана", "last_name": "Дубовець", "middle_name": "Василівна", "birthdate": (2007, 11, 10), "grades": [7, 8, 5, 8, 8, 9, 8, 7, 7, 10]},
    "Nikita_Stroganov": {"first_name": "Микита", "last_name": "Строганов", "middle_name": "Іванович", "birthdate": (2000, 2, 8), "grades": [6, 7, 8, 9, 10, 10, 10, 10, 10, 9]},
    "Karina_Nikolaenko": {"first_name": "Карина", "last_name": "Ніколаєнко", "middle_name": "Петрівна", "birthdate": (2004, 22, 9), "grades": [2, 3, 5, 4, 5, 4, 3, 3, 5, 8]},
    "Eugenia_Dron": {"first_name": "Євгенія", "last_name": "Дрон", "middle_name": "Сергіївна", "birthdate": (2001, 11, 11), "grades": [12, 12, 12, 10, 10, 9, 8, 9, 9, 8]}
}

df = pd.DataFrame(students).T

print(df)

mean_grades = df["grades"].apply(lambda x: sum(x) / len(x))
print("\nСереднє значення оцінок кожного студента:")
print(mean_grades)

sum_grades = df["grades"].apply(sum)
print("\nСума оцінок кожного студента:")
print(sum_grades)
