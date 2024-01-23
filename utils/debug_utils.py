import inspect


def stack_depth():
    return len(inspect.getouterframes(inspect.currentframe())) - 1

