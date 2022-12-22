import time

def heapify(arr, n, i,drawData, timeTick):
   largest = i 
   l = 2 * i + 1 
   r = 2 * i + 2 
   if l < n and arr[i] < arr[l]:
      largest = l
   if r < n and arr[largest] < arr[r]:
      largest = r
   if largest != i:
      arr[i],arr[largest] = arr[largest],arr[i] 
      drawData(arr, ['yellow' if x == largest or x == i else 'blue' for x in range(len(arr))])
      time.sleep(timeTick)
      heapify(arr, n, largest,drawData, timeTick)

def heapSort(arr,drawData, timeTick):
   n = len(arr)
   # maxheap creation
   for i in range(n, -1, -1):
      heapify(arr, n, i,drawData, timeTick)
      
   # element extraction
   for i in range(n-1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i] # swap
      drawData(arr, ['black' if x == i or x == 0 else 'blue' for x in range(len(arr))])
      time.sleep(timeTick)
      drawData(arr, ['green' if x>=i  else 'blue' for x in range(len(arr))])
      time.sleep(timeTick)
      heapify(arr, i, 0,drawData, timeTick)
      
   drawData(arr, ['green' for x in range(len(arr))])
