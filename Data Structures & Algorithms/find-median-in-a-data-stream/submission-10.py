import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # for max heap making sure to negate it
        heapq.heappush(self.max_heap, -1 * num)

        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
            elif len(self.max_heap) < len(self.min_heap):
                heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))
        
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
        
        # edge case
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))

    def findMedian(self) -> float:        
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        
        return self.min_heap[0]
        