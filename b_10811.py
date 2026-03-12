n = 0
m = 0
n, m = map(int, input().split())
basket = []

#상자 갯수 만들기
for _ in range(1,n+1):
    basket.append(_)

# 반복문으로 입력횟수 받기
for i in range(m):
    n, x = map(int, input().split())
    
# 입력받은 값을 사용해 숫자 교환
    basket[n-1:x] = basket[n-1:x][::-1]

# 출력
print(basket)