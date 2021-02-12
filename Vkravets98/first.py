def zima():
    b = 2
    t = int(input('The temperature is: '))
    if t > 0:
        return 'Take off your hat'
    elif t == 0:
        return'Put on your hat'
    else:
        return 'Stay home'
print(zima())

