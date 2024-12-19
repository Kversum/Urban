"""
В качестве введения в сортировку списков на Python вам нужно будет реализовать две функции.
В этом упражнении мы представляем студентов в виде пары (mark, full_name), то есть кортежа из двух элементов.
И в этих упражнениях мы представляем студентов в виде списков пар, например:
students = [(85, "Susan"), (6, "Joshua"), (37, "Jeanette")]
"""


def sort_by_mark(my_class):
    """
    Напишите функцию с именем sort_by_mark,
    которая принимает в качестве аргумента список учащихся и возвращает его копию, отсортированную
    по метке в порядке убывания. Например:
    sort_by_mark(students)
    [(85, "Susan"), (37, "Jeanette"), (6, "Joshua")]
    """
    sort_my_class = sorted(my_class, reverse=True)
    return sort_my_class


def sort_by_name(my_class):
    """
    Напишите функцию с именем sort_by_name, которая принимает в качестве аргумента список учащихся
    и возвращает его копию, отсортированную по имени в порядке возрастания, например:
    sort_by_name(students)
    [(37, "Jeanette"), (6, "Joshua"), (85, "Susan")]
    """
    sort_list = sorted(my_class, key=lambda x: x[1])
    return sort_list


my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada"), (35, "Kir")]
print(sort_by_mark(my_class))
print(sort_by_name(my_class))
