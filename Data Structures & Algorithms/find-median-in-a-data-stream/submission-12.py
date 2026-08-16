import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # target = O(log n)
        heapq.heappush(self.max_heap, -1 * num)

        # we want to maintain roughly equal lengths and if one exists max of 1
        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
        
        # check for a violation
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
        
        # length of the min heap still being more
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # target = O(1)
        max_len = len(self.max_heap)
        min_len = len(self.min_heap)

        # max of max heap and min of min heap represent middle 2 elements
        if max_len == min_len:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        if max_len > min_len:
            return -self.max_heap[0]
        
        return self.min_heap[0]