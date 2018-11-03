def putQueen(tlb, ls, rs, col, deep, n, count):
    if deep == n:
        for i in range(n):
            print(tlb[i])
        count += 1
        return count
    else:
        for i in range(n):
            if ls[deep - i + n] != 1 and rs[i + deep] != 1 and col[i] != 1:
                tlb[i][deep] = 1
                ls[deep - i + n] = 1
                rs[i + deep] = 1
                col[i] = 1
                count = putQueen(tlb, ls, rs, col, deep + 1, n, count)
                tlb[i][deep] = 0
                ls[deep - i + n] = 0
                rs[i + deep] = 0
                col[i] = 0
    return count


if __name__ == "__main__":
    n = int(input("Please input the number of queens: "))
    ls = [0 for i in range(2 * n)]
    rs = [0 for i in range(2 * n)]
    col = [0 for i in range(n)]
    tlb = [[0 for i in range(n)] for i in range(n)]
    count = putQueen(tlb, ls, rs, col, 0, n, 0)
    print("The result is {0}".format(count))
