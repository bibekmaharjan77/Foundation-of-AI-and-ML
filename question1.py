# 1. Write a program to generate all permutations of n 

'''
Design and program idea:

- Permutations are all possible orderings of n items.

- One of the approach is backtracking (recursive swaps)

- the function takes a list of n items and return all possible rearrangements.

Structure of the program:

Using recursion: swaps each element into the current position, then recurse.

Add base case: when at the end, add current list to results.

'''

# Just run the file by python3 question1.py

# backtracking approach

def generate_permutations(arr):
    '''Generate all permutations of the input list arr.'''
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]
    result = []
    backtrack(0)
    return result

# Example
print(generate_permutations([1,2,3])) # outputs: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]
