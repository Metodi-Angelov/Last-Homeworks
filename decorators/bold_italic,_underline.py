def make_bold(fn):
    def wrapper(*args, **kwargs):
        str = '<b>'
        end = '</b>'
        res = fn(*args, **kwargs)
        result = f'{str}{res}{end}'
        return result

    return wrapper


def make_italic(fn):
    def wrapper(*args, **kwargs):
        str = '<i>'
        end = '</i>'
        res = fn(*args, **kwargs)
        result = f'{str}{res}{end}'
        return result

    return wrapper


def make_underline(fn):
    def wrapper(*args, **kwargs):
        str = '<u>'
        end = '</u>'
        res = fn(*args, **kwargs)
        result = f'{str}{res}{end}'
        return result

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
