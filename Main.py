# Напиши функцію split_string, яка приймає рядок і повертає список рядків з двох символів.
# Якщо рядок містить непарну кількість символів, тоді другий символ потрібно замінити на підкреслення ("_").

# Приклад:
#
# split_string("abc") == ["ab", "c_"]
# split_string("abcdef") == ["ab", "cd", "ef"]

# string = "HelloWorld"
# array = list(string)
# print(array)

def split_string(string: str) -> list:

    array = list(string)
    list_length = len(array)
    if list_length % 2 == 1:
        array.append("_")
    else:
        pass
    paired_letters = [array[i] + array[i + 1] for i in range(0, len(array) - 1, 2)]

    return paired_letters

print(split_string("mamamam"))
