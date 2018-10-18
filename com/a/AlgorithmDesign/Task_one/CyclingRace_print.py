import math


def DateTable(num):
    total = int(math.pow(2, num))
    list = []
    for i in range(total + 1):
        list.append([])
    for i in range(total + 1):
        for j in range(total + 1):
            list[i].append(0)
    for i in range(1, total + 1):
        list[1][i] = i

    m = 1

    for i in range(num):
        total = int(total / 2)
        for j in range(1, total + 1):
            for k in range(m + 1, 2 * m + 1):
                for l in range(m + 1, 2 * m + 1):
                    list[k][l + (j - 1) * m * 2] = list[k - m][l + (j - 1) * m * 2 - m]
                    list[k][l + (j - 1) * m * 2 - m] = list[k - m][l + (j - 1) * m * 2]
        m *= 2

    for i in range(1, int(math.pow(2, num)) + 1):
        print(list[i][1:])


num = int(input("Please input K: "))
DateTable(num)
