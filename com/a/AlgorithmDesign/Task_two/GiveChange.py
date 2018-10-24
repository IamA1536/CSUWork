if __name__ == "__main__":
    print("Please input the cash: ", end="")
    r = []
    n = [int(i) for i in input().split(" ")]
    n.sort(reverse=True)

    pay = int(input("Please input the change need: "))

    m = pay
    i = 0

    while n[i] > m:
        i += 1
        del n[i]

    while len(n) > 0:
        while m != 0:
            m = pay
            for i in n:
                if m - i >= 0:
                    m -= i
                    r.append(i)
                else:
                    continue
            if m == 0:
                print("Should pay {0}".format([int(i) for i in r]))
                break
            else:
                r = []
                del n[0]

    if len(r) == 0:
        print("Cannot give the cash")
