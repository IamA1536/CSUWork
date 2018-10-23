if __name__ == "__main__":
    print("Please input the cash: ", end="")
    r = []
    n = [int(i) for i in input().split(" ")]
    n.sort(reverse=True)
    m = int(input("Please input the change need: "))
    i = 0
    while m != 0:
        if i == len(n):
            break
        if n[i] > m:
            i += 1
            continue
        m -= n[i]
        r.append(n[i])
    if m == 0:
        print("Should pay {}".format([int(i) for i in r]))
    else:
        print("Cannot give the cash")
