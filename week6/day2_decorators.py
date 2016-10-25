
def func_caller(func):
    print("i'm in here")
    return func


@func_caller
def remote_control():
    print("i love lamp")
    return 0


remote_control()
#func_caller(remote_control)  # this is what's happening when calling a decorator
