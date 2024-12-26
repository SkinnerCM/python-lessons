#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Function to perform merge sort and store steps
def merge_sort(arr, left, right, steps):
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle, steps)  # Recursively sort left half
        merge_sort(arr, middle + 1, right, steps)  # Recursively sort right half
        merge(arr, left, middle, right, steps)  # Merge the two halves

# Function to merge two halves of the array and record the steps
def merge(arr, left, middle, right, steps):
    left_subarr = arr[left:middle + 1]
    right_subarr = arr[middle + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Merge the two sub-arrays back into arr[]
    while i < len(left_subarr) and j < len(right_subarr):
        if left_subarr[i] <= right_subarr[j]:
            arr[k] = left_subarr[i]
            i += 1
        else:
            arr[k] = right_subarr[j]
            j += 1
        k += 1
        steps.append(arr.copy())  # Append a copy of the array after this step

    # Copy the remaining elements of left_subarr, if any
    while i < len(left_subarr):
        arr[k] = left_subarr[i]
        i += 1
        k += 1
        steps.append(arr.copy())

    # Copy the remaining elements of right_subarr, if any
    while j < len(right_subarr):
        arr[k] = right_subarr[j]
        j += 1
        k += 1
        steps.append(arr.copy())

# Function to update the plot during the animation
def update(frame):
    ax.clear()  # Clear the axes for a clean update
    ax.bar(range(len(frame)), frame)  # Create a bar plot
    ax.set_ylim(0, max(arr) + 1)  # Set y-axis limits to fit the data

# Ask the user for the number of items to sort
n = int(input("Enter the number of items to sort: "))
arr = np.random.randint(1, 100, size=n)  # Random array for sorting
steps = []  # List to store the array states during sorting
merge_sort(arr, 0, len(arr) - 1, steps)  # Perform merge sort and store the steps

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Create the animation
ani = FuncAnimation(fig, update, frames=steps, interval=100)

# Save the animation as a .mp4 file
ani.save('merge_sort_animation.mp4', writer='ffmpeg')

# Alternatively, you can display the animation by showing it directly
# plt.show()