def factorial(num: int):
    print('this recursion no.{}'.format(num))
    if num == 1:
        return 1
    return num * factorial(num-1)


def powFunc(num: int, powVar: int):
    if powVar == 0:
        return 1
    return num*pow(num, powVar-1)


def fib(num: int, result=[], start=0):
    print(f'number of element {len(result)} : ', result)
    if num < 0:
        return []
    elif len(result) == num:
        return result
    elif len(result) > 2:
        result.append(result[len(result)-2]+result[len(result)-1])
    else:
        result.append(start)
    return fib(num, result, start+1)


def sumArray(array: list, idx=0):
    if idx == len(array)-1:
        return array[idx]
    elif len(array) >= 2:
        return array[idx] + sumArray(array, idx+1)
    else:
        array = array[0] if 0 < len(array) < 2 else 0
        return array


if __name__ == '__main__':
    # print(factorial(10))
    # print(powFunc(4,3))
    print('ผลรวม', sumArray(fib(2)))
    # print(sumArray([4, 5, 3, 7, 8, 9]))
