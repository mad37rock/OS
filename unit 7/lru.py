def lru(pages, capacity):
  s = []
  page_faults = 0

  for i in range(len(pages)):
      if pages[i] not in s:
          if len(s) < capacity:
              s.append(pages[i])
          else:
              s.remove(s[0])
              s.append(pages[i])
          page_faults += 1
      else:
          s.remove(pages[i])
          s.append(pages[i])
  return page_faults
print("total pages in faults")                


pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
capacity = 3
print(lru(pages, capacity)) 