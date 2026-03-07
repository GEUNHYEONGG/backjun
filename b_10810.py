f_n, s_n = map(int, input().split())
baskets = [0] * f_n

for _ in range(s_n):

    f_b, s_b, t_nb = map(int, input().split())

    for i in range(f_b-1, s_b):
        baskets[i] = t_nb

print(*baskets)