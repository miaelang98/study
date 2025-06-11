arr = list(input())
arr[1:2] = 'a'
arr[-2:-1] = 'a'

arr = ''.join(arr)
print(arr)