from collections import deque

def fifo_page_replacement(pages, capacity):
    memory = deque(maxlen=capacity)
    page_faults = 0
    page_hits = 0

    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) == capacity:
                memory.popleft()
            memory.append(page)

    hit_ratio = page_hits / len(pages)

    return page_faults, hit_ratio

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3

page_faults, hit_ratio = fifo_page_replacement(pages, capacity)
print("Number of page faults using FIFO algorithm:", page_faults)
print("Hit ratio using FIFO algorithm:", hit_ratio)