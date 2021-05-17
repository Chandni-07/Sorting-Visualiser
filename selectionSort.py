import time
def selection_sort(data, drawData, timeTick):
    for j in range(len(data)):
        min_idx = j

        for i in range(j+1, len(data)):
            if data[i] < data[min_idx]:
                min_idx = i
                drawData(data, ['red' if x == i else 'blue' for x in range(len(data))])
                time.sleep(timeTick)
        data[j], data[min_idx] = data[min_idx], data[j]
        drawData(data, ['green' if x < j else 'blue' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])


