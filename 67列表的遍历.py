def list_while_func():
    """

    :return:
    """
    my_list = ['传值教育', '程序员', 'python']
    i = 0
    while i < len(my_list):
        print(my_list[i])
        i += 1

list_while_func()

def list_for_func():
    my_list = ['传值教育', '程序员', 'python']
    # for i in range(len(my_list)):
    #     print(my_list[i])
    #     i += 1
    for i in my_list:
        print(i)

list_for_func()