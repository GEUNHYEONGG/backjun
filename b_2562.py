num = []
for i in range(9):

    num.append(int(input()))
    
n_max = max(num)
n_list = num.index(n_max)
print(n_max)
print(n_list + 1)