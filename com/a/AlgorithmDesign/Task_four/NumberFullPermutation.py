import math


def permutation(deep, a, b, s):
    if deep == a:
        print(int(s))

    else:
        for i in range(1, a + 1):
            if b[i] != 1:
                s += i * math.pow(10, deep)
                b[i] = 1
                permutation(deep + 1, a, b, s)
                b[i] = 0
                s -= i * math.pow(10, deep)


if __name__ == "__main__":
    a = int(input("Please input the numbers: "))
    b = [0 for i in range(a+1)]
    s = 0
    permutation(0, a, b, s)
