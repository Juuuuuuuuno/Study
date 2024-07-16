# 첫 줄에 T 받고 그 다음줄에 정수 A B를 받는다 
# t= 5 t1 : 1 1 = 2 , t2 12 34 : 46 . . .

a=int(input("값 입력 : "))
c=[]

for _ in range(a):
    x,y=map(int,input().split()) #x,y를 split으로 list로 받는다. 이후 map으로 split을 int형으로 바꾼다.
    c.append(x,y)
    
print(type(c[0]))

for x,y in c:
    print(x+y)

#.append = 배열에 추가
# tuple이 무어싱ㄴ가?
# 리스트는 요소값 변화가 가능하고, 튜플은 요소값 변화가 불가능 하다
# tuple이란? 여러 개의 값을 하나로 묶어 저장할 수 있는 순서가 있는 immutable 자료형이다 -gpt

