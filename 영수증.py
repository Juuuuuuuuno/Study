# 첫째 줄에는 영수증에 적힌 총 금액 X 가 주어진다.
# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
# 이후 N개의 줄에는 각 물건의 가격 a와 개수b가 공백을 사이에 두고 주어진다.

#구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes 출력 아니면 No 출력

x=int(input("총 가격 : "))
n=int(input("물건 개수 : "))
cal = 0

for _ in range(n):
    a,b=map(int,input().split())
    cal += a*b

if(x==cal):
    print("Yes")
else:
    print("No")


# for _ in range = 변수 없이 반복
# map (적용할 요소, 데이터 집합) 배열에서 하나씩 꺼내올때 사용함