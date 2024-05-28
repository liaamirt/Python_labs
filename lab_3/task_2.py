def find_max_consecutive_char(s):
    max_count = 0
    current_count = 1
    max_char = s[0]

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_char = s[i - 1]
            current_count = 1

    if current_count > max_count:
        max_count = current_count
        max_char = s[-1]

    return max_char, max_count

word = input("Введіть слово: ")
char, count = find_max_consecutive_char(word)
print(f"Символ '{char}' повторюється {count} разів підряд найбільше.")
