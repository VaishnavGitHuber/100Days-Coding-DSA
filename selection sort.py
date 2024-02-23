# Selection sort 
def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i 
        for j in range(i,n):
            if array[min_index] > array[j]:
                min_index = j 
        
        if min_index != i:
            array[min_index],array[i] = array[i],array[min_index]
        
    return array 

print(selection_sort([1,9,2,6,3]))