def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return(arr)

N = int(input())
arr = [int(input()) for _ in range(N)]

sorted_arr = bubble_sort(arr)

for i in range(N):
    print(sorted_arr[i])