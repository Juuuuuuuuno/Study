# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

A,B=input("수 입력 : ").split()
A=int(A)
B=int(B)

if(A>B):
    print(">")

    if(A<B):
        print("<")
else:
    print("==")

# 파이썬에서 중첩 의문문은..
# if(A>B):
#    print(">")
# else if(A<B)       <= 이게 아님 그냥 if만 써도 됨

# 수 입력 : 5 1
# Traceback (most recent call last):
#  File "c:\Users\user\Desktop\머학\Study\Study\비교.py", line 4, in <module>
#    A,B=input("수 입력 : ").split                                              <= 여기에 괄호 안적음
# TypeError: cannot unpack non-iterable builtin_function_or_method object
