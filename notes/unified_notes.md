# Unified Notes

This file will hold notes from all of the various materials I will be referencing for this project.
The idea is to organize my notes by topic.
However, if any topic starts to feel "too big" I will move that topic to it's own file.

## Contents by Subject

### Problems

See [problems](./problems.md)

### Topics

- [Arrays](#topic-arrays)
- [Big-O Notation](#topic-big-o-notation)
- [HashTable](#topic-hashtable)
- [Linked Lists](#topic-linked-lists)
- [System Design Fundamentals](#topic-system-design-fundamentals)

### References

* [Introduction to Algorithms - ItA](#introduction-to-algorithms-4th-ed)
* [Cracking the Coding Interview - CtCI](#cracking-the-coding-interview-6th-ed)

## Topic: Arrays

### Problem: Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to
target.

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

Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is
valid.

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
        if the stack is empty (pop returned nothing) or the val doesn't match the cur_char from s
            return false
    if the stack is empty, return true and false otherwise
            
```

## Topic: Hash Table

### CtCi sec IX: Interview Questions ch 1: Arrays and Strings

<dfn>hash table</dfn> - a data structure that maps keys to values for high efficiency lookup

Examples include:

- Python: dictionary
- JavaScript: Object

## Topic: Big-O Notation

### ItA ch 3

<dfn>asymptotic efficiency</dfn> the limit of efficiency as the inputs increase without bounds

An algorithm that is asymptotically more efficient is the best choice for all but the smallest inputs.

Big-O notation characterizes the __upper bound__ on the asymptotic behavior of a function.
This means the function grows no faster than a certain rate, based on the highest order term.

<dfn>Big-O Notation</dfn> - For a given function $g(n)$ we denote $O(g(n))$ by the set of functions:
$$
O(g(n)) = \{ f(n): 0 \leq f(n) \leq cg(n) \forall n \geq n_0 \}
$$
where there exists positive constants $c$ and $n_0$

## Topic: Bitwise Operators

In Python Bitwise operators work on integers and perform operations at the bit level.

### Bitwise Logical Operators

- `&` (AND): Sets each bit to 1 if both bits are 1
- `|` (OR): Sets each bit to 1 if at least one of the bits is 1.
- `^` (XOR): Sets each bit to 1 if only one of the bits is 1.
- `~` (NOT): Inverts all the bits.

### Bitwise Shift Operators

- `<<` (Left Shift):
    - Shifts the bits of the left operand to the left by the number of places specified by the right operand.
- `>>` (Right Shift):
    - Shifts the bits of the left operand to the right by the number of places specified by the right operand.

### Example

```python
a = 10  # 1010 in binary
b = 8  # 0100 in binary
c = 8  # 1000 in binary

print(a & b)  # Output: 0 (0000 in binary)
print(a | b)  # Output: 14 (1110 in binary)
print(a ^ c)  # Output: 2 (0010 in binary)
print(~c)  # Output: -9 (11110110 in binary, using 2's complement)
print(a << 1)  # Output: 20 (10100 in binary)
print(a >> 1)  # Output: 5 (0101 in binary)
```

## Topic: Linked Lists

### Problem Merge: Two Sorted Lists

[LC 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)

#### Pseudocode

```
    Leverage the fact that the lists are sorted
    Loop until reaching the end of one or both lists
        push the smaller value to the new list

    after loop finishes, 
    if one list has remaining nodes
        attach the remaining node(s) to the end of the new list
```

## Topic: System Design Fundamentals

My thoughts based on lectures and other resources mentioned.

### System Design Phases

Times are suggestions but time management is very important.

1. Requirements gathering < 10 min
2. Working Solution < 20 min
3. Deep Dives < 20 Min
4. Wrap up ~ 5 min

### Key Points to Remember

- Have a working solution before you optimize
- Agree with interviewer on basic design
- Draw a high level diagram ASAP
- Draw the user flow
- Don't present DB schema as API schema
- Front End design should be similar but talk about state rather than DB Schema
- Drive the interviewer, this is a positive signal to the interviewer
- Make a note of deep dive topics to come back to
    - It is also a good idea to have topics you won't be talking about
- Time Management
    - Ask for a hint such as "Did I miss anything?" instead of "What are the reqs?"

### Requirements gathering

You need to gather Functional and Non-Functional requirements.
Non-Functional requirements are the so called "ilities" i.e. scalability, availability, reliability, etc.
Functional requirements answer questions about use cases, features and scope.

## References

### Introduction to Algorithms 4th Ed

* by Cormen et. al.
* Abbreviated as #ItA

### Cracking the Coding Interview 6th ed.

* Gayle Laakmann McDowell
* Abbreviated as #CtCI

### System Design Interview – An insider's guide

* By Alex Xu
* Abbreviated as #SDI