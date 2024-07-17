#별찍기 오른쪽 정렬해서 

a=int(input("개수 입력 : "))
n=0

for _ in range(a):
    n=n+1
    print(("★"*n).rjust(a))



# rjust , ljust ( a ), a 자리수 만큼 오른쪽, 왼쪽 정렬 하는 녀석