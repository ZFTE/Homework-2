result = []


def divider(a, b):
    result = 0
    try:
        result = a / b
    except ValueError:
        print("Число дервое меньше чем число второe")
    except IndexError:
        print("Число первае меньше чек число второе")
    except TypeError:
        print("какая-то ршибка")
    except ZeroDivisionError:
        print("ошибочка")
    return result




data = {10: 2,
        2: 5,
        int("123"): 4,
        18: 0,
        int(bool([])): 15,
        8: 4}


for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
