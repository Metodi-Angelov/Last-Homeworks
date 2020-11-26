def type_check(parameter):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, parameter):
                    return 'Bad Type'
            result = fn(*args, **kwargs)

            return result

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
