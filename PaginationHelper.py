# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-09


# TODO: complete this class

class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.len = len(collection)
        self.items_per_page = items_per_page
        self.pages = self.len // items_per_page if self.len % items_per_page == 0 else self.len // items_per_page + 1
        self.isdivisible = self.len % items_per_page == 0

    # returns the number of items within the entire collection
    def item_count(self):
        return self.len

    # returns the number of pages
    def page_count(self):
        return self.pages

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > self.pages - 1:
            return -1
        if self.isdivisible:
            return self.len // self.items_per_page
        else:
            return self.len % self.items_per_page if page_index == self.pages - 1 else self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index == 0 and self.len > 0: return 0
        if self.len == 0:return -1
        if item_index >= self.len or item_index < 0:
            return -1
        if item_index % self.items_per_page != 0:
            return item_index // self.items_per_page
        else:
            return item_index // self.items_per_page - 1


class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        if len(self.collection) % self.items_per_page == 0:
            return len(self.collection) / self.items_per_page
        else:
            return len(self.collection) / self.items_per_page + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= self.page_count():
            return -1
        elif page_index == self.page_count() - 1:
            return len(self.collection) % self.items_per_page or self.items_per_page
        else:
            return self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= len(self.collection) or item_index < 0:
            return -1
        else:
            return item_index / self.items_per_page

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print helper.page_count() # should == 2
print helper.item_count() # should == 6
print helper.page_item_count(0)  # should == 4
print helper.page_item_count(1) # last page - should == 2
print helper.page_item_count(2) # should == -1 since the page is invalid

# page_ndex takes an item index and returns the page that it belongs on
print helper.page_index(5) # should == 1 (zero based index)
print helper.page_index(2) # should == 0
print helper.page_index(20) # should == -1
print helper.page_index(-10) # should == -1 because negative indexes are invalid