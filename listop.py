#create a list of 10 integers
numbers = [12, 45, 7, 23, 89, 34, 56, 78, 1, 90]
def print_list(lst):
    print("List of integers:", lst)

def sum_of_elements(lst):
    total = sum(lst)
    print("Sum of all elements in the list:", total)

def largest_element(lst):
    largest = max(lst)
    print("Largest element in the list:", largest)

def reverse_list(lst):
    reversed_lst = lst[::-1]
    print("List in reverse order:", reversed_lst)
    
def smallest_element(lst):
    smallest = min(lst)
    print("Smallest element in the list:", smallest)

# Call the functions
print_list(numbers)
sum_of_elements(numbers)
largest_element(numbers)
reverse_list(numbers)
smallest_element(numbers)
