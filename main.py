def oneNineTeen():
    a = 1
    while True:
        if a < 20:
            print(a)
            a += 1
        else:
            break
def twentyOne():
    a = 20
    while True:
        if a > 0:
            print(a)
            a -= 1
        else:
            break
def twoTenEven():
    a = 2
    while True:
        if a < 11:
            print(a)
            a += 2
        else:
            break
def nineOneOdd():
    a = 9
    while True:
        if a > 0:
            print(a)
            a -= 2
while True:
    print("oneNineTeen:")
    oneNineTeen()
    print("twentyOne:")
    twentyOne()
    print("twoTenEven:")
    twoTenEven()
    print("nineOneOdd")
    nineOneOdd()
    break