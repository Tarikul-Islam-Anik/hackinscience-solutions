def sort_a_list(a_list):
    return sorted(a_list, reverse=True)


def sort_by_mark(my_class):
    return sorted(my_class, key=lambda mark: mark[0], reverse=True)


def sort_by_name(my_class):
    return sorted(my_class, key=lambda mark: mark[1])
