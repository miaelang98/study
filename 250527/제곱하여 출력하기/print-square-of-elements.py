N = int(input())
numbers = list(map(int,input().split()))
new = [x**2 for x in numbers]
print(*new)