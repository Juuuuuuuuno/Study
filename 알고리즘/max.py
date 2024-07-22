# 최대값 구하기
# 9개의 다른 자연수가 주어질 때 이들 중 최대값을 찾고 몇 번째 수인지 구하기

# 1~9 까지 한 줄에 하나씩 수 입력

lst=[]

for _ in range(9):
    a=int(input("수 입력 : "))
    lst.append(a)
   

print("최대값 : " ,max(lst), "," ,lst.index(max(lst))+1, "째 줄")
