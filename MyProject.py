import random

# Generate a random dataset of 30 integers
data_set = [random.randint(1, 100) for _ in range(30)]

# Function to perform sorting (you can use any sorting algorithm here)
def my_sort(data):
    return sorted(data)

#Sort the dataset
sorted_data = my_sort (data_set)

#Print the original and sorted dataset
print("Original Data:", data_set)
print("Sorted Data:", sorted_data)