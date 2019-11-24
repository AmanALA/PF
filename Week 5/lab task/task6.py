def CubeValues():

    lst = list()
    for i in range(1, 31):
        lst.append(i ** 3)
    print(lst[:6])
    print(lst[-6:])


CubeValues()
