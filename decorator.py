def say_shout(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        func(*args, **kwargs)
        print("After function")
    return wrapper

@say_shout
def hello(word="еда"):
    print(word)

hello("Hi!")