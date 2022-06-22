# Напиши функцію split_string, яка приймає рядок і повертає список рядків з двох символів.
# Якщо рядок містить непарну кількість символів, тоді другий символ потрібно замінити на підкреслення ("_").

# Приклад:
#
# split_string("abc") == ["ab", "c_"]
# split_string("abcdef") == ["ab", "cd", "ef"]

# def split_string(string: str) -> list:
#
#     array=[]
#     array[:0]=string
#     check = len(string)
#     if check % 2 == 0:
#
#             for i in range(0, len(array)-1, 2):
#                 array[i] = array[i] + array[i+1]
#
#     else:
#             array = array.append("_")
#             for i in range(0, len(array)-1, 2):
#                 array[i] = array[i] + array[i + 1]
#
#             return array
#
# print(split_string("mamafa;fa;fja;fa"))

# def split_string(string: str) -> list:
#
#     array=[]
#     array[:0]=string
# #     for i in range(0, len(array)-1, 2):
# #         array[i] = array[i] + array[i+1]
# #
# #     return array
# #
# # print(split_string("mamama"))
#
# print(split_string("mamama"))

string_list = ["a", "b", "c", "d", "f"]

list_length = len(string_list)
paired_list = [string_list[i] + string_list[i+1] for i in range(0, list_length-1, 2)]
if list_length % 2 == 1:
    paired_list.append("_")

print(paired_list)