# Unified Notes

This file will hold notes from all of the various materials I will be referencing for this project.
The idea is to organize my notes by topic. 
However, if any topic starts to feel "too big" I will move that topic to it's own file.

## Contents

### Problems
- [Two Sum](#problem-two-sum)

### Topics
- [Arrays](#topic-arrays)
- [Big-O Notation](#topic-big-o-notation)

### References
* [Introduction to Algorithms - ItA](#introduction-to-algorithms-4th-ed)
* [Cracking the Coding Interview - CtCI](#cracking-the-coding-interview-6th-ed)


## Topic: Arrays

### Problem: Two Sum
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

The key points to consider here are: 
1. There is one valid solution
2. You cannot use the same element twice

The idea is to find which pair of numbers add up to the target value. This is straightforward arithmatic.
We solve this by looping over the array.
As we loop we store compliments in a hashmap with the compliment as the key and the index 
as the value like so:`{<compliment>: <index>}`
In Python a `dict` will work for storage. 
Before storing the value, we check if the current num is a key in the hashmap. 
If it is, return the value from the hashmap and the current index.

#### Complexity Analysis
**Time Complexity: O(n)**
- we loop through the array once. 
- The loop will stop early in many cases but that won't matter
  - call the items we don't traverse c
  - 0 <= c <= n-2
  - This translates to O(n-c) which is equivalent to O(n)

**Space Complexity: O(n)** 
  - the hashmap holds n-1 items
    - this is equivalent to O(n)

### Problem: Valid Parentheses
Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid.

Psuedocode
```
    Create a map with the open chars as the keys and the closing chars as the values
    Check that the first char in s is in the map and return false if not
    initialize a stack
    loop over the chars in s
        if the current char is in the map 
            add the value of from the map to the stack
        else
        pop the last value from the stack 
        if the stack is empty (there is nothing to pop) or the value doesn't match the current char from s
            return false
    if the stack is empty, return true and false otherwise
            
```

## Topic: Big-O Notation

### ItA ch 3
<dfn>asymptotic efficiency</dfn> the limit of efficiency as the inputs increase without bounds

An algorithm that is asymptotically more efficient is the best choice for all but the smallest inputs.

Big-O notation characterizes the __upper bound__ on the asymptotic behavior of a function. 
This means the function grows no faster than a certain rate, based on the highest order term.

<dfn>Big-O Notation</dfn> - For a given function $g(n)$ we denote $O(g(n))$ by the set of functions:
$$
O(g(n)) = \{ f(n): 0 \leq f(n) \leq cg(n) \forall n \geq n_0  \}
$$
where there exists positive constants $c$ and $n_0$
## References

### Introduction to Algorithms 4th Ed
* by Cormen et. al.
* Abbreviated as ItA

### Cracking the Coding Interview 6th ed.
* Gayle Laakmann McDowell
* Abbreviated as CtCI