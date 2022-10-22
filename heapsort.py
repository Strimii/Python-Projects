def heap(array, n, parent): 
    largest = parent
    l = 2 * parent + 1 
    r = 2 * parent + 2 
    
    if l < n and array[parent] < array[l]: 
        largest = l 
  
    if r < n and array[largest] < array[r]: 
        largest = r 
  
    if largest != parent: 
        array[parent], array[largest] = array[largest], array[parent] 
        heap(array, n, largest) 
        
def heapsort(array): 
    n = len(array) 
  
    for i in range(n//2 - 1, -1, -1): 
        heap(array, n, i) 
  
    for i in range(n-1, 0, -1): 
        array[i], array[0] = array[0], array[i] 
        heap(array, i, 0) 
        
array = input()            
array = array.split()
heapsort(array) 
n = len(array)
print(' '.join(array))
