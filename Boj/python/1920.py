def binary_search(n):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if arr_a[mid] == arr_b[n]:
            results[n] = 1
            return
        elif arr_a[mid] > arr_b[n]:
            end = mid - 1
        else:
            start = mid + 1

N = int(input())
arr_a = list(map(int, input().split()))
arr_a.sort()
M = int(input())
arr_b = list(map(int, input().split()))
results = [0 for _ in range(M)]

for i in range(M):
    binary_search(i)

for result in results:
    print(result)