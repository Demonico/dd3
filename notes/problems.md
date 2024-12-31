# Select Problems By Topic

## Dynamic Programming

### LC 740 Delete and Earn

It turns out this problem is a disguised version of a classic DP problem "House Robber".

#### Problem Statement

You are given an integer array `nums`. You want to maximize the number of points you get by performing the following
operation any number of times:

* Pick any `nums[i]` and delete it to earn `nums[i]` points. Afterwards, you must delete every element equal to
  `nums[i] - 1` and every element equal to `nums[i] + 1`.

Return the maximum number of points you can earn by applying the above operation some number of times.

#### My Approach

1. Build a points list
    1. This will be similar to an adjacency list for BFS problems.
    2. $points[i] = \sum i \forall i \in nums$
2. Loop over the range in points and build the dp list such that:
    1. $dp[i] = max(dp[i-1], dp[i-2] + points[i])$
    2. This can be further optimized to use two pointers instead of the `dp` list

#### Why this works

The points list represents the number of points we get for taking any specific value from nums.
By arranging them sequentially we can see them next to the neighbors we can't take i.e. `i + 1` and `i - 1`.

## Heaps

### LC 973 K Closest Points to Origin

My solution: [LC 973 K Closest Points to Origin](week2/lc/973.py)

#### My Approach

1. Loop over all points
2. Calculate their distance to the origin `(0,0)`
3. Add the distances to a heap `(dist,point)` and return K smallest from the heap