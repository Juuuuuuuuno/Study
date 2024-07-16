# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫 줄에 T값 받고 T값 만큼 a+b 출력

t=int(input("값 입력 : "))
s=[]
n=0

for _ in range(t):
    a,b=map(int,input().split())
    s.append((a,b))

for a,b in s:
    n=n+1
    print("Case #",n,":",a+b)