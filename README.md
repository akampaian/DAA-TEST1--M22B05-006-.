Task 2: Analysis
Working Principle of Insertion Sort:
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort is often used for small data sets or partially ordered data. The algorithm works by iteratively expanding a sorted portion of the array and inserting the next element into its proper place.

comparing question 1 
no 4
Insertion sort is generally less efficient than more advanced algorithms for large datasets. 
Bubble sort has a similar efficiency, but merge sort is typically more efficient for larger datasets. 
However, for small datasets or nearly sorted datasets,
insertion sort can outperform other algorithms due to its simplicity and lower overhead.

Task 5: Practical Scenario
Insertion sort is a good choice for a nearly sorted list with just a few elements out of order. This is because insertion sort has a linear time complexity in the best case when the array is nearly sorted. The overhead of more complex algorithms may not be justified for small or nearly sorted lists, making insertion sort a practical choice in such scenarios.

psedocode qst 2

function find_max(arr):
    
if length of arr is 0:
 return "Array is empty"
    
max_value = arr[0]
    
for i from 1 to length of arr - 1:
if arr[i] > max_value:
 max_value = arr[i]
    
return max_value


questio 2
no 3

Complexity Analysis:
Time Complexity: O(n) - The algorithm iterates through the array once, making a constant-time comparison for each element.
Space Complexity: O(1) - The algorithm uses only a constant amount of additional space regardless of the size of the input array.




