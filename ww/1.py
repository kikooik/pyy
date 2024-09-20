n = int(input())

s1 = 0
s2 = 0
l = []

for _ in range(n):
    x = int(input())
    l.append(x)
    
for i in l:
    if (i > 0):
        s1 += i
    if (i < 0):
        s2 += i
        
print(s1, s2)
