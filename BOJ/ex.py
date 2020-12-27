n = int(input())
nList = list(map(int, input().split()))
nList.sort(reverse=True)
ans = 0
ansList = []
'''
맨 앞에는 중간수가 들어가야하고
그 다음부터는 n의 홀짝에 따라 다름

n이 짝수일 경우
중간수, 작 큰 작 ...

n이 홀수일 경우
중간수, 큰 작 ...
'''


def initList(k):
    global ansList
    ansList = []
    ansList.append(k)


def func1():
    f = 0  # 앞
    b = n - 1  # 뒤
    for i in range(n - 1):
        if i % 2 == 0:
            # 작은 수 넣기 (뒤)
            ansList.append(nList[b])
            b -= 1
        else:
            # 큰 수 넣기 (앞)
            ansList.append(nList[f])
            f += 1
    getAns(ansList)


def func2():
    f = 0  # 앞
    b = n - 1  # 뒤
    for i in range(n - 1):
        if i % 2 == 1:
            # 작은 수 넣기 (뒤)
            ansList.append(nList[b])
            b -= 1
        else:
            # 큰 수 넣기 (앞)
            ansList.append(nList[f])
            f += 1
    getAns(ansList)


def getAns(ansList):
    global ans
    cnt = 0
    for i in range(n-1):
        cnt += abs(ansList[i] - ansList[i + 1])
    ans = max(ans, cnt)


if n % 2 == 0:
    initList(nList[n // 2 - 1])
    func1()
    initList(nList[n // 2 - 1])
    func2()
else:
    initList(nList[n // 2])
    func1()
    initList(nList[n // 2])
    func2()


print(ans)
