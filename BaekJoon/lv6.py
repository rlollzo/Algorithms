from logging.config import stopListening


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
    word_len = 0
    word_len = len(word)
    word = list(word)

    for i in range(round(int(word_len)/2)):
        word_len -= 1
        if word[i] != word[word_len]:
            print(0)
            break
        if i == len(word)-1:
            print(1)
Q10988()