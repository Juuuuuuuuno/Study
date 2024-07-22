# 시험점수
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

A=int(input(" 성적 입력 : "))

if(90<=A<=100):
    print("A")

elif(80<=A<=89):
    print("B")

elif(70<=A<=79):
    print("C")

elif(60<=A<=69):
    print("D")

else:
    print("F")


# 왜 값대로 안나오고  F로 나옴??
# 왜지?
# https://dojang.io/mod/page/view.php?id=2222 이 Tlqkf이 중첩 의문문 이상하게 씀..
# elif 쓰면 됨