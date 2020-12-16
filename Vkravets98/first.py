def zima():
    t = int(input('The temperature is: '))
    if t > 0:
        return 'Take off your hat'
    elif t == 0:
        return'Put on your hat'
    else:
        return 'Stay home'
print(zima())

def summa(x,y):
    return x+y
print(summa(5,7))
