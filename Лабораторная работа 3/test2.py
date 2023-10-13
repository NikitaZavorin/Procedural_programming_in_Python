# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2):
    spl_str1 = str1.split("|")
    spl_str2 = str2.split("|")
    set_str1 = set(spl_str1)
    set_str2 = set(spl_str2)
    inter = set_str1.intersection(set_str2)
    return sorted(list(inter))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))
