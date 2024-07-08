#나머지 값 출력
#a, b, c값을 입력받고 첫줄에 (a+b)%c 둘째 ((a%c)+(b%c))%c 셋째((a%c)x(b%c)) 넷째 ((A%C) × (B%C))%C출력

a=int(input("값 입력 : "))
b=int(input("값 입력 : "))
c=int(input("값 입력 : "))

print( ((a+b)%c) )
print( ((a%c)+(b%c))%c )
print( ((a%c)*(b%c))%c )
print( ((a%c)*(b%c))%c )

#중간에 10번째 줄 안나오는 오류가 있었는데 오탈자였음 해결