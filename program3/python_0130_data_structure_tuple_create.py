'''

--------------------
tuple
--------------------

tuple is highly-similar to list.

Differences between tuple and list:

1) list is mutable, tuple is immutable.
   Once a tuple is created, you cannot change it.

2) You use [] in list, you use () in tuple

'''


def create_tuple_example():

    print("empty tuple and empty list -----------------------")
    tup_empty = ()
    list_empty = []
    print(tup_empty)
    print(list_empty)

    print("single value tuple and list ----------------------")
    tup_1 = (50,) # comma is mandatory as (50) is same as 50
    list_1 = [50]
    print(tup_1)
    print(list_1)

    print("multiple values tuple and list ----------------------")
    tup_multiple = (1, 2, 3, 4, 5)
    list_multiple = [1, 2, 3, 4, 5]
    print(tup_multiple)
    print(list_multiple)

    list_multiple[0] = -1
    print(list_multiple)

    # tup_multiple[0] = -1 # error! because, tuple is immutable

    print("multiple values tuple and list ----------------------")
    tup_mix1 = ('a', True, 10, tup_multiple)
    list_mix1 = ['a', True, 10, list_multiple]
    print(tup_mix1)
    print(list_mix1)

    # IMPORTANCE!! ----------------------------------
    # For tuple, you can omit the parentheses!
    tup_mix1 = 'a', True, 10, tup_multiple
    print(tup_mix1)
    # -----------------------------------------------


    print("Concatenate tuple and list -------------------------------")
    list_compo1 = list_empty + list_1 + list_multiple + list_mix1
    print(list_compo1)

    tup_compo1 = tup_empty + tup_1 + tup_multiple + tup_mix1
    print(tup_compo1)

    tup_compo2 = tup_empty, tup_1, tup_multiple, tup_mix1
    print(tup_compo2)
    # create a new tuple using 4 new tuple values, it is the same as :
    # tup_compo2 = (tup_empty, tup_1, tup_multiple, tup_mix1)

    print('duplicate tuple --------------------------------------')
    zeros_tuple = (0,) * 100
    print(zeros_tuple)

    int_var = (0) * 100
    print(int_var) # this is int value - 0


    print("Another interesting example --------------------------")
    value1 = 3 * (40 + 2)
    print(f"3 * (40 + 2) is of type： {type(value1)}, its value is: {value1}")

    value2 = 3 * (40 + 2,)
    print(f"3 * (40 + 2,) is of type： {type(value2)}, its value is: {value2}")


    print("Create a tuple from a list ----------------------------")
    tup_from_list = tuple(list_compo1)
    print(tup_from_list)

    print("Create a tuple from a range ---------------------------")
    tuple_from_range = tuple(range(0,100,5))
    print(tuple_from_range)

    print("Create a tuple from a str -----------------------------")
    tup_from_str = tuple("Python")
    print(tup_from_str)


create_tuple_example()