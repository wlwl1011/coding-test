n, x = map(int, input().split())
arr = input().split()

for i in range(n):
    a = int(arr[i])
    if x>a:
        print(a, end=" ")