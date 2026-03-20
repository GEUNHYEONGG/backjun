b_n, c_n = map(int, input().split())

b_v = list(range(1, b_n + 1))

for _ in range(c_n):

    n_b_n, roof = map(int, input().split())
    
    b_v[n_b_n-1] , b_v[roof-1] = b_v[roof-1], b_v[n_b_n-1]

print(*b_v)