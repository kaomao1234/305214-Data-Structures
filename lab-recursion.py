def factorial(num: int, result=1):
    if num == 0:
        return result
    else:
        result *= num
    return factorial(num-1, result=result)


def sumArray_func(array: list, sumArray=0, length=0):
    if length == len(array):
        return sumArray
    sumArray += array[length]
    return sumArray_func(array, sumArray, length+1)


def fib_func(num: int, start=[0, 1], lenght=1):
    start.append(start[lenght]+start[lenght-1])
    if len(start) == num:
        return start
    return fib_func(num, start, lenght+1)


def pow_func(num: int, pow: int, sum_pow=1):
    if pow == 0:
        return sum_pow
    sum_pow = sum_pow*num
    return pow_func(num, pow-1, sum_pow)


if __name__ == '__main__':
    print(fib_func(20))