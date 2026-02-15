def finish_me(func):

    def wrapper(*args):
        func(*args)
        print("finished")
    return wrapper


@finish_me
def print_me(text):
    print(text)


print_me("print me")
