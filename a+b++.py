# a+b 값 받은만큼  a+b 마지막 입력은 0 0

t=int(input("값 입력 : "))
cal=[]


for _ in range(t):
    a,b=map(int,input().split())
    cal.append((a,b))

print("0 0")

for a,b in cal:
    print(a+b)


