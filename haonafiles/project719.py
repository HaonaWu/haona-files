def is_even(num):
    if num % 2 ==0:
        print("True")
        return True
    else:
        print("False")
        return False

is_even(0)


def calc_total(list):
    sum = 0
    For num in list:
        sum += num
    print sum
    return sum

list = ["2, 3, 4, 5, 9 , 89"]
calc_total(list)
