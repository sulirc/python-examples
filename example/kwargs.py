# def kwargs_func(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))


# # Driver code
# kwargs_func(first='Geeks', mid='for', last='Geeks')


def args_func(*args, **kwargs):
    print("*args", *args)
    print("**kwargs", kwargs.items())

    for arg in args:
        print("argument through *args :", arg)

    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


def args_func_HOF(*args, **kwargs):
    print(">>> HOF")
    first = kwargs.get("first")
    print("get first value from kwargs", first)

    del kwargs["first"]
    # new_kwargs = 
    # for key, value in kwargs.items():
    #   if key == "first":
    #     print('Hey! ', key, value)
    #     del kwargs[key]

    args_func(*args, **kwargs)

args_func_HOF(1, 2, 3, first='Geeks', mid='for', last='Geeks')

