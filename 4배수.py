# 혜아가 N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하라
# 4 => long int             8 => long long int

# 4로 나눴을 때 1 이면 long 2 면 long long
a=int(input("정수 입력 : "))


if(a//4):
    n=a//4
    print("long "*n,"int")

#// 몫 연산자