class ListFunctions:
    def __init__(self, lst):
        if not lst:
            raise ValueError("The list is empty.")
        self.lst = lst

    def maximum(self):
        return max(self.lst)

    def minimum(self):
        return min(self.lst)

    def sum_all(self):
        return sum(self.lst)

    def average(self):
        return sum(self.lst) / len(self.lst)

    def median(self):
        sorted_lst = sorted(self.lst)
        n = len(sorted_lst)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
        else:
            return sorted_lst[mid]
        
# module_SetOperations.py

class SetOperations:
    def __init__(self, s1, s2):
        self.set1 = s1
        self.set2 = s2
    
    def add_element(self, element):
        self.set1.add(element)
    
    def remove_element(self, element):
        self.set1.discard(element)

    def union_intersection(self):
        union = self.set1.union(self.set2)
        intersection = self.set1.intersection(self.set2)
        return union, intersection

    def difference(self):
        return self.set1.difference(self.set2)

    def is_subset(self):
        return self.set1.issubset(self.set2)

    def set_length(self):
        count = 0
        for _ in self.set1:
            count += 1
        return count

    def symmetric_difference(self):
        return self.set1.symmetric_difference(self.set2)

    def power_set(self):
        power_set_list = [[]]
        for element in self.set1:
            power_set_list += [subset + [element] for subset in power_set_list]
        return [set(subset) for subset in power_set_list]

    def unique_subsets(self):
        def generate_subsets(current, index):
            if index == len(self.set1):
                subsets.append(set(current))
                return
            generate_subsets(current, index + 1)
            generate_subsets(current + [list(self.set1)[index]], index + 1)

        subsets = []
        generate_subsets([], 0)
        return subsets


# dict_operations.py

class DictOperations:
    def __init__(self, *dicts):
        self.dicts = dicts
    
    def merging_dict(self):
        merged = {}
        for d in self.dicts:
            if isinstance(d, dict):
                merged.update(d)
            else:
                raise TypeError("All arguments must be dictionaries")
        return merged

    def common_keys(self):
        if not self.dicts:
            return set()
        common = set(self.dicts[0].keys())
        for d in self.dicts[1:]:
            if isinstance(d, dict):
                common.intersection_update(d.keys())
            else:
                raise TypeError("All arguments must be dictionaries")
        return common

    def invert_dict(self, d):
        if not isinstance(d, dict):
            raise TypeError("Argument must be a dictionary")
        
        inverted = {}
        for key, value in d.items():
            if value in inverted:
                if isinstance(inverted[value], list):
                    inverted[value].append(key)
                else:
                    inverted[value] = [inverted[value], key]
            else:
                inverted[value] = key
        return inverted

    def common_key_value_pairs(self):
        if not self.dicts:
            return set()
        
        common_pairs = set(self.dicts[0].items())
        for d in self.dicts[1:]:
            if isinstance(d, dict):
                common_pairs.intersection_update(d.items())
            else:
                raise TypeError("All arguments must be dictionaries")
        return common_pairs

# LibraryManager.py

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, publisher, volume, year, isbn):
        if isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        self.books[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': year,
            'isbn': isbn
        }

    def remove_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book with this ISBN does not exist.")
        del self.books[isbn]

    def get_book_details(self, isbn):
        return self.books.get(isbn, "Book not found.")

    def search_books(self, query):
        results = []
        for book in self.books.values():
            if query.lower() in book['title'].lower() or query.lower() in book['author'].lower():
                results.append(book)
        return results

    def list_books(self):
        return list(self.books.values())

    def update_book(self, isbn, **kwargs):
        if isbn not in self.books:
            raise ValueError("Book with this ISBN does not exist.")
        self.books[isbn].update(kwargs)

    def check_availability(self, isbn):
        return isbn in self.books
