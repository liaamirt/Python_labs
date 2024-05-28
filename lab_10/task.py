try:
    # Відкриваємо файл 'questions.txt' у режимі запису ('а')
    with open('questions.txt', 'a') as file:
        # Запитуємо у користувача прізвище
        surname = input("Введіть ваше прізвище: ")

        question = input("Введіть ваше питання з програмування мовою Python: ")

        # Записуємо прізвище у файл
        file.write(surname + '\n')
        # Записуємо питання у файл
        file.write(question + '\n')

    # Якщо все пройшло успішно, виводимо повідомлення про успішне завершення запису
    print("Дані успішно записано у файл questions.txt")
except IOError:
    # В разі виникнення помилки виводимо повідомлення про невдалу спробу запису у файл
    print("Помилка: не вдалося записати дані у файл")
