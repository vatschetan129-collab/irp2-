arr = list(map(int, input("Enter sorted array elements: ").split()))

target = int(input("Enter target: "))

low = 0
high = len(arr) - 1

result = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        result = mid
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

print("Index:", result)