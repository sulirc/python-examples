# def kwargs_func(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))


# # Driver code
# kwargs_func(first='Geeks', mid='for', last='Geeks')


def args_func(*args, **kwargs):
    for arg in args:
        print("argument through *args :", arg)

    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
args_func(1, 2, 3, first='Geeks', mid='for', last='Geeks')
