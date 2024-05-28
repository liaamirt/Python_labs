def insert_after_element(lst, target, new_element):
    try:
        index = lst.index(target)
        lst.insert(index + 1, new_element)
    except ValueError:
        print(f"Елемент {target} не знайдено в списку.")
    return lst

def print_list(lst):
    print("Список:", lst)


input_list = input("Введіть елементи списку через пробіл: ").split()

input_list = [int(i) for i in input_list]

target_element = int(input("Введіть елемент, після якого потрібно вставити новий елемент: "))

new_element = int(input("Введіть новий елемент: "))

updated_list = insert_after_element(input_list, target_element, new_element)

print_list(updated_list)
