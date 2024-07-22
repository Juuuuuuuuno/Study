# 오븐 시간 구하기

h=int(input("시간 입력 :"))
m=int(input("분 입력 : "))
t=int(input("타이머 설정 : "))


if(0<=m<=59):
    temp=m
    m=m+t

    if(t>=60 and m>=60):
        temp=m
        m=m-60

        if(m==60):
            m=0
            print(h+2,m)

        else:
            print(h+1,m)

    if(t>=60 or m>=60):

        if(m==60):
            m=0
            print(h+1,m)

        if(m>=60):
            temp=m
            m=m-60
            h=h+1

            if(h==24):
                h=0
                print(h,m)

    else:
        print(h,m)
