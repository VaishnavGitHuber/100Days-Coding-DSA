def bubble_sort(array):
    n = len(array)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j+1] < array[j]:
                array[j+1],array[j] = array[j],array[j+1]
        
    return array 

print(bubble_sort([3,9,1,2,5]))