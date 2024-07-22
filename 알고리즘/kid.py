# 꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!
# 첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.

A,B,C=input("값 입력 : ").split() # string으로 저장됨
A=int(A)
B=int(B)
C=int(C)

print(A+B+C)



# File "c:\Users\user\Desktop\머학\Study\Study\kid.py", line 4, in <module>
# A,B,C=int(input("값 입력 : ")).split()
# ValueError: invalid literal for int() with base 10: '77 77 7777'

# 왜 안될까? -> A,B,C=int(input("값 입력 : ")).split() 이게 문제인거 같았음
# A,B,C=input("값 입력 : ").split()
# print(A+B+C)
# 이렇게 하니깐 77777777 이렇게 출력 되는거임! 왜 그러지 하니깐 변수를 int로 설정하니 잘 나옴

#input을 여려개 받으려면 .split()을 이용하면 됨