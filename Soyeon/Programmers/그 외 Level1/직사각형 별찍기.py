a, b = map(int, input().strip().split(' '))

stars =''

for _ in range(b):
    for _ in range(a):
        stars +='*'
    stars +='\n'
    
print(stars)