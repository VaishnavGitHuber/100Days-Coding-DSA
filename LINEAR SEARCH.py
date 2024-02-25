def linear_search(array,key):
    found = False
    for x in array:
        if x == key:
            found = True
            break 
    return found

array = [23,89,76,21,5]
key = 89

if linear_search(array,key):
    print("Key is found")
else:
    print("Key is not found")
        