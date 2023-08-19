import copy
import sys
sys.stdin = open('./0) 문법-1.input', encoding="utf-8")


def printResult(func):
    def printFunTitle(description):
        print("="*50)
        print(f"{func.__name__} : {description}")
        print("="*50)

    def inner(description):
        for _ in range(2):
            print()
        printFunTitle(description)
        for _ in range(3):
            """
            =======================
            Case1 입력
            =======================
            이부분 없애기 위해. Input파일에서 어떤 input이 어떤 케이스 인풋인지 보기 좋게
            하기 위한 내용으로 실제 data가 아님
            """
            input()
        print(func())
        for _ in range(2):
            """
            input들과 구분을 위해 줄바꿈 두번이 있음.
            실제 data가 아님. 
            """
            input()

    return inner


####################################
# case1 : 문자열 1개 입력받아서 처리시
####################################

@printResult
def case1():
    return input().strip()  # 양쪽 white space(공백, 엔터) 제거
    # --> "    공백제거"로 input파일에는 되어 있지만
    # "공백제거"로 출력된다.


case1('공백제거')

#########################################
# case2 :  문자열 여러개 한줄에 공백 기준으로 입력
#########################################


@printResult
def case2():
    return input().split()  # 공백 기준 리스트로 분류, strip() 생략 가능

    # "1 2 3 4 5"로 input 파일에 되어 있는데
    # 공백 기준으로 split하여 리스트 생성
case2('문자열 여러개 공백 기준으로 입력- 문자열 리스트')


#####################################
# case 3: 정수 한개 입력
#####################################
@printResult
def case3():
    return int(input())


case3('정수 한개 입력')

#####################################
# 정수 여러개 입력
#####################################


@printResult
def case4():
    s = input().split()
    return list(map(int, s))


case4('정수 여러개 입력 - int형 리스트')


@printResult
def case4_2():
    return list(map(int, input().split()))


case4_2('정수 여러개 입력 - int형 리스트(2)')

# map(func, s)    # s의 각 원소 x에 대해 func(x) 값으로 변환
#                 # iterator 반환


#####################################
# 3줄을 입력받아 리스트 만들기
#####################################


@printResult
def case5():
    li = []
    for i in range(3):
        li.append(input().strip())
    return li


case5('3줄을 입력받아 *문자열* 리스트 만들기')


@printResult
def case5_2():
    return [input().strip() for _ in range(3)]


case5_2('3줄을 입력받아 *문자열* 리스트 만들기(2)')


#####################################
# 3줄을 입력받아 리스트 만들기
#####################################


@printResult
def case6():
    return [int(input()) for _ in range(3)]


case6('3줄을 입력받아 *int형* 리스트 만들기')


#####################################
# 3줄을 입력받아 리스트 만들기, 한 줄에 여러 문자있음
#####################################


@printResult
def case7():
    return [input().split() for _ in range(3)]


case7('3줄을 입력받아 *문자열* 리스트 만들기 - 2차원리스트')


#####################################
# 3줄을 입력받아 리스트 만들기, 한 줄에 여러 문자있음
#####################################


@printResult
def case8():
    return [list(map(int, input().split())) for _ in range(3)]


case8('3줄을 입력받아 *int형* 리스트 만들기 - 2차원리스트')


print("="*50)
print("리스트 할당 print")
print("="*50)
# print
li = [1, 2, 3, 4, 5]
print(li)
print(*li)   # 1 2 3 4 5
print(*li, sep=' ', end='\n')
print(*li, sep='', end='')
print()
print(*li, sep='\n')


print("="*50)
print("리스트 할당 f-string")
print("="*50)
# f-string : 'li = [1,2,3,4,5]'
print(f'li = {li}')
print(f'li[3:] = {li[3:]}')
print('li = {}'.format(li))
print('li = {}{}'.format(li, li[3:]))

print("="*50)
print("1차원 배열 생성")
print("="*50)
# 1차원 배열 생성
li = [0] * 10
li[0] = 10
print(li)


print("="*50)
print("2차원 배열 생성 - [0,0,0] 3개 같은 주소")
print("="*50)
# 2차원 배열 생성
# X
li = [[0]*3] * 3
for item in li:
    print(id(item))
li[0][0] = 10  # [0,0,0] 3개가 모두 같은 id라서 [0][0]만 바꿔도 3개 모두 10으로 바뀜
print(li)


print("="*50)
print("2차원 배열 생성 - [0,0,0] 3개 다른 주소")
print("="*50)
# O
li = [[0]*3 for _ in range(3)]
for item in li:
    print(id(item))
li[0][0] = 10  # 반복을 하면서 만들어준거라서 id가 달라... 그래서 제일 앞 1개만 바뀜
print(li)


print("="*50)
print("3차원 배열 생성 - [0,0,0,0] 3개 다른 주소")
print("="*50)
# 3차원 배열 생성
li = [[[0]*4 for _ in range(3)] for _ in range(2)]
print(li)


l1 = [1, 2, 3]
print("="*50)
print(f"리스트 copy    {l1}")
print("="*50)
# 1d. copy

# reference copy
print("-"*50)
print("reference copy")
print("-"*50)
l2 = l1
print(f"l2=l1   l2 --> {id(l2)}")
print(f"l2=l1   l1 --> {id(l1)}")
print("-"*50)
print("shallow copy")
print("-"*50)
# shallow copy
l3 = l1.copy()
print(f"l3에 l1.copy()    l3 --> {id(l3)}")
l3 = l1[:]
print(f"l3 = l1[:]     l3---> {id(l3)}")


l1 = [[0, 0], [1, 1], [2, 2]]
print("="*50)
print(f"2D 리스트 copy    {l1}")
print("="*50)
# 2d. copy

# reference copy
print("-"*50)
print("reference copy")
print("-"*50)
l2 = l1
print(f"l2=l1   l2 --> {id(l2)}")
print(f"l2=l1   l1 --> {id(l1)}")
print("-"*50)
print("shallow copy")
print("-"*50)
# shallow copy
l3 = l1.copy()
print(f"l3에 l1.copy()    l3 --> {id(l3)}")
l3 = l1[:]
print(f"l3 = l1[:]     l3---> {id(l3)}")
# 일차원 껍데기는 주소가 다를지 몰라도, 각 요소 [0,0], [1,1] , [2,2]는 주소가 같아

print("-"*50)
for item in l1:
    print(f"l1의 요소들의 id ---> {id(item)}")
print("-"*50)
print("-"*50)
for item in l3:
    print(f"l3의 요소들의 id ---> {id(item)}")
print("-"*50)

# deep copy
# 그래서 완전히 독립적인 리스트로 copy하려면
l4 = copy.deepcopy(l1)
print("-"*50)
for item in l4:
    print(f"l4의 요소들의 id ---> {id(item)}")
print("-"*50)

# if , while false 조건
# None, False
# 0, 0.0, ..
# empty collection : (), [], {}, set(), ''

if not ():
    print(1)

# x,y = 0,1
# if x or y   # x ture 이면 y 확인 안함
# if x and y  # x false 이면 y 확인 안함

# x if C else y   # C 참이면 x, 거짓이면 y 반환
print(1 if () else 0)
