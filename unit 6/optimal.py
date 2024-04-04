def optimal_page_replacement(pages, capacity):
  memory = []
  page_faults = 0
  page_hits = 0

  for i, page in enumerate(pages):
      if page in memory:
          page_hits += 1
      else:
          if len(memory) < capacity:
              memory.append(page)
          else:
              # Find the page that will not be used for the longest period of time
              farthest_page = -1
              farthest_index = -1
              for j, mem in enumerate(memory):
                  if mem not in pages[i+1:]:
                      farthest_page = mem
                      farthest_index = j
                      break
              if farthest_page != -1:
                  memory[farthest_index] = page
              else:
                  memory[0] = page
              page_faults += 1

  hit_ratio = page_hits / len(pages)

  return page_faults, hit_ratio

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3

page_faults, hit_ratio = optimal_page_replacement(pages, capacity)
print("Number of page faults using Optimal algorithm:", page_faults)
print("Hit ratio using Optimal algorithm:", hit_ratio)