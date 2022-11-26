import random
import time
x = input()
x=x.split(" ")

data1 = x
data2 = x

total1 = 0
total2 = 0

def quicksortrandom(arr, first , last):
    
    if(first < last):
        pivotindex = partitionrandrandom(arr, first, last)
        quicksortrandom(arr , first , pivotindex-1)
        quicksortrandom(arr, pivotindex + 1, last)
        
def partitionrandrandom(arr , first, last):
  
    randpivot = random.randrange(first, last)
    arr[first], arr[randpivot] = arr[randpivot], arr[first]
    return partitionrandom(arr, first, last)
  
def partitionrandom(arr,first,last):
    
    pivot = first # pivot
    i = first + 1 
    for j in range(first + 1, last + 1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
  
start1 = time.perf_counter()     #start testu dla randomizedquicksort
quicksortrandom(data1, 0, len(data1) - 1)
end1 = time.perf_counter()   #koniec testu lowercase
total1 += end1 - start1

print(data1)
print("Uœredniony czas testu randomizedquicksort ", "{0:02f}s".format(total1))



def partition(arr, f, l):

    pivot = arr[l]
    i = f - 1
    for j in range(f, l):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
            (arr[i + 1], arr[l]) = (arr[l], arr[i + 1])
    return i + 1

def quicksort(arr, f, l):

    if f < l:
        q = partition(arr, f, l)
        quicksort(arr, f, q - 1)
        quicksort(arr, q + 1, l)
 
 
start2 = time.perf_counter()     #start testu dla quicksort
quicksort(data2, 0, len(data2) - 1)
end2 = time.perf_counter()   #koniec testu quicksort
total2 += end2 - start2

print(data2)
print("Uœredniony czas testu quicksort ", "{0:02f}s".format(total2))