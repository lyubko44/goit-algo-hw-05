def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0
  
    while low <= high:
        count +=1 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return (count, arr[mid])
 
    # якщо елемент не знайдений
    return (count, arr[mid])

arr = [2, 3, 4.2, 10, 11.5, 12, 40]
x = 11.5
result = binary_search(arr, x)
print(f"Result {result} (iterations, result) has been found for a given number: {x}")