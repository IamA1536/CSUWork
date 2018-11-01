def put(w, v, n, c):
    s = [[-1 for i in range(c + 1)] for i in range(n + 1)]
    for i in range(c + 1):
        s[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            s[i][j] = s[i - 1][j]
            if s[i - 1][j] < s[i - 1][j - w[i - 1]] + v[i - 1] and j >= w[i - 1]:
                s[i][j] = s[i - 1][j - w[i - 1]] + v[i - 1]
    for i in s:
        del i[0]
    return s


if __name__ == "__main__":
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    for i in put(w, v, len(w), 10):
        print(i)
