def tags(tag):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            str = f'<{tag}>'
            end = f'</{tag}>'
            res = fn(*args, **kwargs)
            result = f'{str}{res}{end}'
            return result

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
