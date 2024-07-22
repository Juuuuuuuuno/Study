# 첫번째 N과 X가 주어진다. 
# 두번째 N의 값 A를 입력
# X보다 작은 수를 순서대로 공백으로 구분해 출력

i=input("두 수 입력").split()

n=-1
m=0

# lst=[i[0]]

llst=[]
lst=list(map(int,input().split()))

for _ in lst:
    n=n+1
    m=i[1]

    if(lst[n]<int(m)):
        llst.append(lst[n])
    else:
        pass

print(*llst)

# pass = 넘어가