# 첫 줄에 T 받고 그 다음줄에 정수 A B를 받는다 
# t= 5 t1 : 1 1 = 2 , t2 12 34 : 46 . . .

a=int(input("값 입력 : "))
c=[]

for _ in range(a):
    x,y=map(int,input().split()) #x,y를 split으로 list로 받는다. 이후 map으로 split을 int형으로 바꾼다.
    c.append((x,y)) #c[]이라는 한 가지 값에 x,y라는 값 2개가 저장이 되기 때문에 c[] 타입이 list가 아닌 tuple형으로 저장됨
    

for x,y in c: #c의 데이터 타입이 tuple이기 때문에 for문의 변수도 x,y로 두 값을 받는것이다.
    print(x+y)

#.append = 배열에 추가
# tuple이 무어싱ㄴ가?
# 리스트는 요소값 변화가 가능하고, 튜플은 요소값 변화가 불가능 하다
# tuple이란? 여러 개의 값을 하나로 묶어 저장할 수 있는 순서가 있는 immutable 자료형이다 -gpt

