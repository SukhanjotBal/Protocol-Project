import collections 
from collections import Counter
import heapq 

def Huffman(text):
    Counter_check = Counter(text)
    heap = []
    for i, (char, count) in enumerate(Counter_check.items()):
        heap.append(count, i , char)
    heapq.heapify(heap)
    next_id = len(heap)
    while len(heap) > 1:
        w1, _, left = heapq.heappop(heap)
        w2, _, right = heapq.heappop(heap)
        merged = (left, right)
        next_id += 1
        heapq.heappush((w1+w2), next_id, merged)
    return heap[0][2]