def factorial(num: int):
    print('this recursion no.{}'.format(num))
    if num == 1:
        return 1
    return num * factorial(num-1)


def powFunc(num: int, powVar: int):
    if powVar == 0:
        return 1
    return num*pow(num, powVar-1)


def fibonance(num: int, result=[], start=0):
    if len(result) < 2:
        result.append(start)
        fibonance(num, result, start+1)
    elif len(result) == num:
        return result
    print(result)
    result.append(result[start-2]+result[start-1])
    return fibonance(num, result)


def sumArray(array: list, idx=0):
    if idx == len(array)-1:
        return array[idx]
    return array[idx] + sumArray(array, idx+1)


if __name__ == '__main__':
    # print(factorial(10))
    # print(powFunc(4,3))
    print(fibonance(10))
    # print(sumArray([4, 5, 3, 7, 8, 9]))