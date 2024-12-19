# Unified Notes

## Topic: Arrays

### Problem: Two Sum
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