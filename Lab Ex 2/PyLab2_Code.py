#Question 1 code
print("-----------------Question 1 code-------------------")

from PyLab2_QuesModules import ListFunctions
lst = [10, 20, 30, 40, 50, 60, 70]

def Functions_Exmp(lst):
    func = ListFunctions(lst)
    print("List:",lst)
    print("Maximum:", func.maximum())
    print("Minimum:", func.minimum())
    print("Sum:",func.sum_all())
    print("Average:",func.average())
    print("Median:",func.median())
    print()

Functions_Exmp(lst)

print("-----------------------------------------------------")

# #Question 2 code
print("\n------------------Question 2 code-------------------\n")
# main_SetOperations.py

from PyLab2_QuesModules import SetOperations

def set_operations():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    
    ops = SetOperations(set1, set2)
    
    print("Initial sets:")
    print("Set1:", ops.set1)
    print("Set2:", ops.set2)
    print()

    ops.add_element(4)
    print("Set1 after adding 4:", ops.set1)

    ops.remove_element(2)
    print("Set1 after removing 2:",ops.set1)

    union, intersection = ops.union_intersection()
    print("Union of Set1 and Set2:", union)
    print("Intersection of Set1 and Set2:", intersection)

    diff = ops.difference()
    print("Difference of (Set1 - Set2):", diff)

    subset_check = ops.is_subset()
    print("Is Set1 a subset of Set2?", subset_check)

    length = ops.set_length()
    print("Length of Set1:", length)

    sym_diff = ops.symmetric_difference()
    print("Symmetric Difference of Set1 and Set2:", sym_diff)

    power_set_result = ops.power_set()
    print("Power Set of Set1:", power_set_result)

    unique_subsets_result = ops.unique_subsets()
    print("Unique Subsets of Set1:", unique_subsets_result)

set_operations()
print("\n------------------------------------------------------\n")

# #Question 3 code
# print("-------------------Question 3 code----------------------\n")

from PyLab2_QuesModules import DictOperations

def dict_operations():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'a': 1, 'd': 5, 'e': 6}

    ops = DictOperations(dict1, dict2)

    # a. Merging dictionaries
    merged = ops.merging_dict()
    print("Merged Dictionary:")
    print(merged)
    print()
    
    # b. Common keys
    common = ops.common_keys()
    print("Common Keys:")
    print(common)
    print()
    
    # c. Inverting a dictionary
    inverted = ops.invert_dict(dict1)
    print("Inverted Dictionary:")
    print(inverted)
    print()
    
    # d. Common key-value pairs
    common_pairs = ops.common_key_value_pairs()
    print("Common Key-Value Pairs:")
    print(common_pairs)
    print()

dict_operations()
print("---------------------------------------------------------\n")


# print("----------------------Question 4 code----------------------\n")
# main.py
from PyLab2_QuesModules import LibraryManager

def library_manager():
    library = LibraryManager()
    
    library.add_book("Operating Systems", "Andrew S. Tanenbaum", "Pearson", "1st", 2021, "9780134211314")
    library.add_book("Data Structures and Algorithms", "Narasimha Karumanchi", "CareerMonk", "3rd", 2022, "9789388424315")
    library.add_book("Machine Learning with Python", "Chris Albon", "O'Reilly Media", "1st", 2023, "9781492032642")
    
    # Remove a book
    library.remove_book("9789388424315")
    
    # Retrieve book details
    print("Details of a book with ISBN 9780134211314:", library.get_book_details("9780134211314"))
    
    # Search for books
    print("Search results for 'Machine Learning':", library.search_books("Machine Learning"))
    
    # List all books
    print("All books in the library:", library.list_books())
    
    # Update book details
    library.update_book("9780134211314", volume="2nd", year=2024)
    
    # Check book availability
    print("Is the book with ISBN 9780134211314 available?", library.check_availability("9780134211314"))

# Run the demonstration
library_manager()

print("\n-------------------------------------------------------------------\n")

#Question 5 code
print("----------------------Question 5 code----------------------\n")

weather_data = [
    {"date": "2024-07-22", "max_temp": 35, "min_temp": 25, "humidity": 80},
    {"date": "2024-07-23", "max_temp": 32, "min_temp": 24, "humidity": 70},
    {"date": "2024-07-24", "max_temp": 30, "min_temp": 22, "humidity": 65},
    {"date": "2024-07-25", "max_temp": 28, "min_temp": 21, "humidity": 60},
    {"date": "2024-07-26", "max_temp": 33, "min_temp": 23, "humidity": 75},
    {"date": "2024-07-27", "max_temp": 36, "min_temp": 26, "humidity": 85},
    {"date": "2024-07-28", "max_temp": 34, "min_temp": 24, "humidity": 77}
]

# Function to find the highest and lowest temperatures recorded during the week
def find_extreme_temperatures(data):
    max_temp = max(day['max_temp'] for day in data)
    min_temp = min(day['min_temp'] for day in data)
    return max_temp, min_temp

# Function to determine the number of days with temperatures above 30°C
def count_days_above_30(data):
    count = sum(1 for day in data if day['max_temp'] > 30)
    return count

# Function to compute the average humidity over the specified period
def average_humidity(data):
    total_humidity = sum(day['humidity'] for day in data)
    average = total_humidity / len(data)
    return average

# Main
highest_temp, lowest_temp = find_extreme_temperatures(weather_data)
days_above_30 = count_days_above_30(weather_data)
avg_humidity = average_humidity(weather_data)

print(f"Highest Temperature: {highest_temp}°C")
print(f"Lowest Temperature: {lowest_temp}°C")
print(f"Number of days above 30°C: {days_above_30}")
print(f"Average Humidity: {avg_humidity:.2f}%")

print("--------------------------------------------------------")