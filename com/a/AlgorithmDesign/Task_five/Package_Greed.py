def greed(c, w, v):
    sum = 0
    cp = [[v[i], w[i], v[i] / w[i]] for i in range(len(w))]
    cp.sort(reverse=True, key=lambda x: x[2])
    for i in range(len(v)):
        if cp[i][2] == cp[i + 1][2]:
            if cp[i][1] > cp[i + 1][1]:
                cp[i][1], cp[i + 1][1] = cp[i + 1][1], cp[i][1]
    i = 0
    while i < len(cp):
        if w[i] <= c:
            c -= w[i]
            sum += v[i]
        i += 1
    print("The result with greed is {0}".format(sum))


if __name__ == "__main__":
    c = int(input("Please input the volume of package: "))
    print("Please input the weight: ")
    w = [int(i) for i in input().split(" ")]
    print("Please input the value: ")
    v = [int(i) for i in input().split(" ")]
    greed(c, w, v)
