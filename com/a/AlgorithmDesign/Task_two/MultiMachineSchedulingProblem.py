if __name__ == "__main__":
    m = int(input("The number of machine: "))
    print("Please input the time of work: ", end="")
    w = [int(i) for i in input().split(" ")]
    w.sort(reverse=True)
    max = w[0]
    d = [max]
    del w[0]

    for i in range(1, m):
        j = 0
        sum = 0
        while sum <= max and j < len(w):
            if sum + w[j] <= max:
                sum += w[j]
                del w[j]
            else:
                j += 1
        d.append(sum)
    d.sort()
    w.sort(reverse=True)
    if len(w) != 0:
        j = 0
        if len(d) > len(w):
            for i in range(len(w)):
                d[i] += w[i]
        else:
            for i in range(len(w)):
                d[j] += w[i]
                if j < len(d) - 1:
                    j += 1
                else:
                    j = 0
    print(d)
