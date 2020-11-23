def fibonacci():
    curr_num = 0
    prev_num = 1
    while True:
        yield curr_num
        curr_num, prev_num = prev_num, curr_num + prev_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
