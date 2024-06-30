# goit-algo-hw-09

Greedy Algorithms and Dynamic Programming

Explanation and comparison of the considered algorithms

Greedy algorithm
Time complexity: O(n), where n is the number of coin denominations.
Spatial complexity: O(1), only a few variables for denominations and result dictionary.
Performance: Very fast and efficient in most practical applications. It makes decisions locally at every step, choosing the largest coin possible. However, it does not always provide an optimal solution for all coin systems (it works perfectly for standard coin systems such as the one used in this example).

Dynamic programming
Time complexity: O(n * amount), where n is the number of coin denominations and amount is the change amount.
Space Complexity: O(quantity), due to the table used to store the minimum number of coins for each amount.
Efficiency: Guarantees to find the optimal solution (minimum number of coins), but at the cost of greater time and space complexity. This method is more suitable when coin denominations do not follow a simple pattern that allows the greedy algorithm to work optimally.

Application
Greedy algorithm: fast and simple, but does not always provide an optimal solution for coins with non-standard denominations.
Dynamic programming: slower and more resource-intensive, but guarantees an optimal solution.

For large amounts, the greedy algorithm works much faster, but may not always be optimal. The dynamic programming approach, although slower, ensures the use of a minimum number of coins, making them more reliable in scenarios with complex coin systems.

Example Performance Comparison

![alt text](image.png)