mu_lis = []

def add_list(pa):
    mu_lis.append(pa)
    print(mu_lis)

for it in range(6):
    add_list(it)

print(*mu_lis, sep=' ')


def add_list(pa):
    lis = []
    for it in range(pa):
        lis.append(it)
    print(lis)
    return lis

newlis = add_list(6) 
print(*newlis, sep=' ')
