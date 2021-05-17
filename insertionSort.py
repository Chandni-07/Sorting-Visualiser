
import time

def insertion_sort(data,drawData, timeTick):

    for i in range(1, len(data)):

        t = i
        j = i - 1
        while j >= 0 and data[t] < data[j]:
            data[j],data[t]=data[t],data[j]
            j -= 1
            t -= 1
            drawData(data, ['black' if x == j or x == t else 'blue' for x in range(len(data))])
            time.sleep(timeTick)
        drawData(data, ['green' if x < i else 'blue' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])

