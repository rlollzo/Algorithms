from idlelib.autocomplete import TRY_F


def Q27866():
    print("Q. 27866")
    s = input()
    n = int(input())
    n -=1
    print(s[n])

def Q2743():
    print("Q. 2743")
    s = input()
    print(len(s))

def Q9086():
    print("Q. 9086")
    num = input()
    for i in range(int(num)):
        s = input()
        p = (s[0]+s[len(s)-1])
        i -= 1
        print(p)

def Q11654():
    print("Q. 11654")
    s = input()
    print(ord(s))

def Q11720():
    print("Q. 11720")
    total = 0
    n = input()
    s = input()
    for i in range(int(n)):
        total += int(s[i])
    print(total)

def Q10809():
    print("Q. 10809")
    s = input()
    a = []
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in arr:
        tft = True
        for j in range(len(s)): #baekjoon
            if i == s[j]:
                a.append(j)
                tft = False
                break
        if tft == True:
            a.append(-1)
    print(a)
    print(*a)
    # print(*map(input().find,map(chr,range(97,123))))


def Q2675():
    print("Q. 2675")
    s = input()

def Q1152():
    print("Q. 1152")
    s = input().split()
    print(len(s))

def Q2908():
    a, b = input().split()
    a =int(str(a)[::-1])
    b =int(str(b)[::-1])
    result = a if a > b else b
    print(result)


def Q2675():
    print("Q. 2675")
    result = []
    case = int(input())
    for c in range(case):
        paragraphs = ''
        num, word = input().split()
        num = int(num)
        for s in word:
            paragraphs += s*num
        result.append(paragraphs)

def Q11718():
    print("Q. 11718")
    while True:
        try:
            print(input())
        except EOFError:
            break

def Q5562():
    print("Q. 5562")
    phone = input()
    time = 0
    for s in phone:
        if s == 'A' or s == 'B' or s == 'C':
            time += 2 + 1
        elif s == 'D' or s== 'E'or s== 'F':
            time += 3 + 1
        elif s ==  'G'or s=='H'or s=='I' :
            time += 4 + 1
        elif s ==  'J'or s=='K'or s=='L' :
            time += 5 + 1
        elif s == 'M'or s== 'N'or s=='O' :
            time += 6 + 1
        elif s ==  'P'or s=='Q'or s=='R'or s=='S' :
            time += 7 + 1
        elif s == 'T'or s=='U'or s=='V' :
            time += 8 + 1
        elif s == 'W'or s=='X'or s== 'Y'or s=='Z' :
            time += 9 + 1
    print(time)
Q5562()