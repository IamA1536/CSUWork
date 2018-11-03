import copy

global best
global now
global bestl
global nowl
global f1
global f2
best = 10000000
now = 0
bestl = []
nowl = []
f1 = 0
f2 = 0


def shceduling(a, deep, n):
    global best
    global now
    global bestl
    global nowl
    global f1
    global f2
    if deep == n:
        if best > now:
            best = now
            bestl = copy.deepcopy(nowl)
    else:
        for i in range(deep, n):
            f1 += a[0][nowl[i]]
            temp = f2
            f2 = max(f1, f2) + a[1][nowl[i]]
            now += f2
            if now < best:
                nowl[deep], nowl[i] = nowl[i], nowl[deep]
                shceduling(a, deep + 1, n)
                nowl[deep], nowl[i] = nowl[i], nowl[deep]
            f1 -= a[0][nowl[i]]
            now -= f2
            f2 = temp


if __name__ == "__main__":
    print("Plesae input the number of work: ", end="")
    n = int(input())
    print("Input the time table: ")
    a = []
    nowl = [int(i) for i in range(n)]
    bestl = copy.deepcopy(nowl)
    for i in range(2):
        a.append([int(j) for j in input().split(" ")])

    shceduling(a, 0, n)
    print("The time of best scheduling is {0} : \n {1} ".format(best, bestl))
