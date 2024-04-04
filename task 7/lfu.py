def lfu(pages, capacity):
  s, faults, freq = [], 0, {}

  for page in pages:
      if page not in s:
          if len(s) == capacity:
              min_freq_page = min(s, key=lambda x: freq.get(x, 0))
              s.remove(min_freq_page)
              del freq[min_freq_page]
          s.append(page)
          faults += 1
      else:
          s.remove(page)
          faults += 1
      freq[page] = freq.get(page, 0) + 1

  return faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3
page_faults = lfu(pages, capacity)
print("Number of page faults:", page_faults)
