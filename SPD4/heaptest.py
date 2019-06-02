import heap_max
import heap_min

aheap = heap_max.Heap_max(1)
bheap = heap_min.Heap_min(1)
if (aheap.is_empty()):
    print("hi")
for item in [[5, 2], [10, 3], [2, 20], [2, 1], [2, 25], [20, 22], [9, 7]]:
    aheap.insert(item)
    bheap.insert(item)
if (aheap.is_empty()):
    print("hi")
# Zdejmowanie elementów ze sterty od największego do najmniejszego.
while not aheap.is_empty():
    a = aheap.remove()
    print(a)
print('\n')
while not bheap.is_empty():
    b = bheap.remove()
    print(b)
