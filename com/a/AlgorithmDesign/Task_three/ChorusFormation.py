import copy


def picktosort(w):
    if len(w) == 0:
        return 0
    s = [1 for i in range(len(w))]
    for i in range(len(w)):
        for j in range(i):
            if w[j] <= w[i]:
                s[i] = max(s[i], s[j] + 1)
    return s


if __name__ == "__main__":
    print("Please intput the hight of students: ", end="")
    a = [int(i) for i in input().split(" ")]
    b = copy.deepcopy(a)
    a.reverse()

    al = picktosort(b)
    ar = picktosort(a)
    ar.reverse()
    for i in range(len(al)):
        ar[i] += al[i] - 1
    print("We should pick {0} student(s) at least.".format(len(a) - max(ar)))
