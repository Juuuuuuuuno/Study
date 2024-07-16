# 첫 줄에 T 받고 그 다음줄에 정수 A B를 받는다 
# t= 5 t1 : 1 1 = 2 , t2 12 34 : 46 . . .

a=int(input("값 입력 : "))
c=[]

for _ in range(a):
    x,y=map(int,input().split())
    c.append((x,y))

for x,y in c:
    print(x+y)

#.append = 배열에 추가

