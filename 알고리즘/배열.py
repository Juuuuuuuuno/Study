# 배열 개수 세기
# N개 정수 주어졌을때 v가 몇개인지 구하기

# 첫번째 배열 크기 입력     두번째 배열값 입력       세번째 찾는 값이 몇개인지 출력


a=int(input("정수 입력 : "))

lst=list(map(int,input().split()))
# lst라는 list를 만듦 input().split()으로 값을 문자로 받아서 list에 저장하는데 map을 이용해 이것을 int로 바꿈 근데 그럼 type이 map이 됨
# 이게 list(map(int,input().split()))이 list가 map type을 list로 바꿈 그래서 count가 사용 가능해짐

print(type(lst))

b=int(input("찾을 값 : "))

print(lst.count(b))

# 두번째 줄의 조건인 한 줄에 배열에 넣을 값 입력을 하려면 반복문을 쓰면 안됨
# map에는 count를 적용할 수 없음 => list(map(int,input().split()))으로 사용하면 type이 map에서 list로 바뀜 => count 사용 가능

'''
AttributeError: 'map' object has no attribute 'count'
'''