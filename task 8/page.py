class PageTable:
  def __init__(self, capacity):
      self.capacity = capacity
      self.page_table = []

  def page_fault(self, page):
      if page in self.page_table:
          return False
      else:
          if len(self.page_table) == self.capacity:
              print("Page fault for page {}, replacing frame {} with page {}".format(page, self.page_table[0], page))
              self.page_table.pop(0)
          self.page_table.append(page)
          return True


def simulate_paging(pages, page_table_size):
  page_table = PageTable(page_table_size)
  page_faults = sum(page_table.page_fault(page) for page in pages)
  print("Total Page Faults:", page_faults)


pages = [0, 1, 2, 3, 0, 4, 1, 0, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
page_table_size = 3

simulate_paging(pages, page_table_size)
