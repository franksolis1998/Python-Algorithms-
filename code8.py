def to_jaden_case(string):
    list = string.split()
    new_list = [i.capitalize() for i in list]
    print(new_list)
    return " ".join(new_list)
