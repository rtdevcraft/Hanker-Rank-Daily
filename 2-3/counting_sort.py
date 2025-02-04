arr=[1,1,3,2,1]

def countingSort(arr): 
    frequency_array = [0] * 100 
    for i in arr: 
        frequency_array[i] += 1 
    return frequency_array

result = countingSort(arr)
print(result)