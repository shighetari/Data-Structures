import time
from singly_linked_list import LinkedList

n = 100000

l = []
ll = LinkedList()

for i in range(n):
    l.append(i)
    ll.add_to_tail(i)

start_time = time.time()
for i in range(n):
    l.pop(0)
end_time = time.time()
print(f"List pop from front took {end_time} - {start_time} seconds ")
