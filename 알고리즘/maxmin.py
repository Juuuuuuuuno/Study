# 정수가 주어진다. 최대 최소값 구해라

# 첫째 줄에는 N개의 정수가 주어진다.                # 둘째 줄엔 N개의 정수를 공백으로 구분해 주엉진다.
# 정수 N개의 최대값과 최소값을 공백으로 구분해 출력한다.


a=int(input("정수 입력 : "))

b=list(map(int,input().split())) #split()으로 한 줄에 띄어쓰기를 기준으로 값을 받음 (문자) => map으로 split()을 int로 바꾸는데 값이 map으로 되어 있음 => list가 map을 list로 변환 시킴

print(min(b), max(b))