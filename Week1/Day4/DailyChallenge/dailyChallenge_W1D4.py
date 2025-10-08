# Daily Challenge : Pagination
import math

class Pagination():  # class to present paginated content
    def __init__(self,items=None,page_size=10):
        self.items=items
        self.page_size=page_size
        if self.items==None:
            self.items=[]
        self.current_idx=0 #current page index
    def total_pages(self):
        # print(f"len(self.items) is {len(self.items)}")
        # print(f"page size is {self.page_size}")
        total=math.ceil(len(self.items)/self.page_size)
        # print(f"total page is {self.total_page}")
        # return math.ceil(len(self.items)/self.page_size)
        return total
    
    def get_visible_items(self):
        # self.current_idx=current_page
        start = self.current_idx * self.page_size
        end = start + self.page_size  #nb : end exclu
        return self.items[start:end]

 # --- Navigation ---
#  go_to_page(page_num)
# → Goes to the specified page number (1-based indexing); If page_num is out of range, raise a ValueError.
    def go_to_page(self, page_num):
        tp=self.total_pages()
        self.last_error=None
        try:
            if 1 <= page_num <= tp:
                self.current_idx = page_num - 1  # 1-based -> 0-based
            else:
                raise ValueError("page_num is out of range")
        except Exception as e:
            self.last_error = f"Invalid page_num: {e}"
            print(self.last_error)
        return self

    
    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        tp=self.total_pages()
        self.current_idx = tp - 1
        return self

    def next_page(self):
        tp=self.total_pages()
        if self.current_idx < tp - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
# bonus : Add a Custom __str__() Method
# This magic method should return a string displaying the items on the current page, each on a new line.
    def __str__(self):
        return "\n".join(map(str, self.get_visible_items()))


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(0)
# Raises ValueError

p.go_to_page(10)
print(p.current_idx + 1)
# Output: ValueError

