arr = [10, 25, 5, 40, 15]

minimum = arr[0]

for i in range(1, len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]

print(minimum)