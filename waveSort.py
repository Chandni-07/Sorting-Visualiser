import time

def sortInWave(arr, drawData,timeTick):
    n=len(arr)
    for i in range(0, n, 2):
        drawData(arr, ['black' if x==i  else 'blue' for x in range(len(arr))])
        time.sleep(timeTick)

        if (i> 0 and arr[i] < arr[i-1]): #i is small then left
            arr[i],arr[i-1] = arr[i-1],arr[i]
            drawData(arr, ['red' if x==i  else 'blue' for x in range(len(arr))])
            time.sleep(timeTick)
            time.sleep(timeTick)

        if (i < n-1 and arr[i] < arr[i+1]):#i is small then right
            arr[i],arr[i+1] = arr[i+1],arr[i]
            drawData(arr, ['green' if x==i  else 'blue' for x in range(len(arr))])
            time.sleep(timeTick)
            time.sleep(timeTick)

    drawData(arr, ['green' if x%2!=0  else 'red' for x in range(len(arr))])
