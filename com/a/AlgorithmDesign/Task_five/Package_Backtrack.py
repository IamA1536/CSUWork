global sum
sum = 0


def backtrack(c, v, w, deep, now):
    global sum
    if deep == len(w):
        sum = max(sum, now)
        return None
    for i in range(deep, len(v)):
        if c >= w[i]:
            now += v[i]
            c -= w[i]
            backtrack(c, v, w, deep + 1, now)
            c -= w[i]
            now -= v[i]
        backtrack(c, v, w, deep + 1, now)


if __name__ == "__main__":
    c = int(input("Please input the volume of package: "))
    print("Please input the weight: ")
    w = [int(i) for i in input().split(" ")]
    print("Please input the value: ")
    v = [int(i) for i in input().split(" ")]
    backtrack(c, v, w, 0, 0)
    print("The result with backtrack is {0}".format(sum))
