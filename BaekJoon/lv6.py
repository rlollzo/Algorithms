def Q25083():
    print('Q25083')
    print('         ,r\'\"7')
    print('r`-_   ,\'  ,/')
    print(' \\. ". L_r\'')
    print('   `~\\/')
    print('      |')
    print('      |')

def Q3003():
    print('Q3003')
    a = input().split()
    king = 1-int(a[0])
    queen = 1-int(a[1])
    look = 2- int(a[2])
    bishop = 2-int(a[3])
    night = 2-int(a[4])
    phone = 8-int(a[5])
    print(king,queen,look,bishop,night, phone)

def Q2444():
    print('Q2444')
    star = int(input())
    down = star
    a = 1
    for i in range(star):
        for i in range(star-1, 0, -1):
            print(' ', end="")
        for j in range(a):
            print('*', end="")
        a += 2
        star -= 1
        print()
    a -= 4
    star = 1
    for i in range(down):
        for k in range(star):
            print(' ', end="")

        for j in range(a):
            print('*', end="")
        a -= 2
        star += 1


        if down == star:
            exit()
        print()

def Q10988():
    print('Q10988')
    word = input()
    word_len = len(word)
    word = list(word)

    for i in range(round(int(word_len)/2)):
        word_len -= 1
        if word[i] != word[word_len]:
            print(0)
            break
        if i == len(word)-1:
            print(1)


def Q1157():
    print('Q1157')
    word = input()
    word = word.upper()
    alpahbet = ''.join(set(word.upper()))
    max = 0
    result = ''
    for i in range(len(alpahbet)):
        current = word.count(alpahbet[i])
        if max < current:
            max = current
            result = alpahbet[i]
        elif max == current and result != alpahbet[i]:
            result = '?'
    print(result)

def Q2941():
    print('Q2941')
    word = input()
    croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    num = 0
    for i in croatia:
        if word.count(i):
            num += word.count(i)
            word = word.replace(i, ' ')
    print(len(word.replace(' ',''))+num)

def Q1316():
    print('Q1316')
    num = input()
    count = 0
    for i in range(int(num)):
        word = input()
        for j in range(len(word)):
            before = word
            word = word.replace(word[0],' ')
            word = word.lstrip()
            if len(word)==0:
                count += 1
                break
            elif word.count(' '):
                break
    print(count)


def Q25206():
    print('Q25206')
count, total = 0,0
total_score = 0
for i in range(19):
    data = input().split()
    score = float(data[1])
    rating = data[2]
    if rating == 'A+':
        total += score * 4.5
        total_score += score
    elif rating == 'A0':
        total += score * 4.0
        total_score += score
    elif rating == 'B+':
        total += score * 3.5
        total_score += score
    elif rating == 'B0':
        total += score * 3.0
        total_score += score
    elif rating == 'C+':
        total += score * 2.5
        total_score += score
    elif rating == 'C0':
        total += score * 2.0
        total_score += score
    elif rating == 'D+':
        total += score * 1.5
        total_score += score
    elif rating == 'D0':
        total += score * 1.0
        total_score += score
    elif rating == 'F':
        total_score += score
if total != 0:
    print(round(total/total_score,6))
else:
    print("0.000000")

Q25206()
