
## Union Function
- traver each link list and add element in a set (only save unique element)
- sort then append to return link list

### Reasoning Behind Decisions:
- to union, we need combine both link list, only unique element so, using set in python is useful

### Time Efficiency:
- Best: O(n1 + n2), Average: O(n1 + n2 + n log n), Worst: O(n1 + n2 + n^2)

### Space Efficiency:
- O(min(n1, n2)) - set only save unique element in both link link

## Intersection Function
- intialize 2 set to save unique element for both link list
- trasve one link list and check the existence in other one
- append the same element in return link list

### Reasoning Behind Decisions:
- to know 1 element exist in 2, check one by one in both set of data

### Time Efficiency:
- Best: O(1), Average: O(n1 + n2 + n log n), Worst: O(n1 * n2 + n log n)
Average case: O(n1 + n2 + n log n) (assuming amortized constant time for set.add)

### Space Efficiency:
- O(min(n1, n2))