# https://www.acmicpc.net/source/7800702
# 30724 kb, 128 ms
a, b = map(int, input().split())
num_of_factors = [0] * (b + 1)

for n in range(2, b + 1):
    if num_of_factors[n] == 0:
        factor = n
        while factor <= b:
            for i in range(factor, b + 1, factor):
                num_of_factors[i] += 1
            factor *= n
            
num_of_underprimes = 0
for count in num_of_factors[a:]:
    if num_of_factors[count] == 1:
        num_of_underprimes += 1
        
print(num_of_underprimes)