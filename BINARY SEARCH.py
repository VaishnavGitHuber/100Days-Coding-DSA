# Binary seatch 
def binary_search(array,key):
    l = 0
    r = len(array)-1
    found = False
    
    while(l <= r):
        mid = (l+r)//2
        if array[mid] == key:
            found = True
            break
        elif key < array[mid]:
            r = mid -1
        else:
            l = mid + 1 
            
    return found 
# Sorted array
array = [3,6,19,67,123]
key = 67

if binary_search(array,key):
    print("Key is found")
else:
    print("Key is not found")
    

    