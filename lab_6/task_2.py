def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def print_list(lst):
    print("Список:", lst)

input_list = input("Введіть елементи списку через пробіл: ").split()
input_list = [int(i) for i in input_list]
sorted_list = quicksort(input_list)
print_list(sorted_list)
