def find_max(arr):
    if not arr:
        return "Array is empty"
    
    max_value = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    
    return max_value
print(find_max([3, 7, 1, 9, 5]))  
print(find_max([]))               
print(find_max([8])) 