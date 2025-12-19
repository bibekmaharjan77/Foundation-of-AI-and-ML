'''
Design Idea
- A combination picks m distinct items from n, regardless of order.

- Recursion: choose/not choose each item.

- Using indices to avoid duplicates and ensures choices are in order.

Structure of the program:

- It starts at the first index.

- If the current combination reaches length m, add it to results.

- For each step, either include or skip the current element.

'''

# Just run the file by python3 question2.py

# Combination generator: backtracking approach
def generate_combinations(arr, m):
    '''Generate all combinations of m elements from arr.'''
    def backtrack(start, comb):
        if len(comb) == m:
            result.append(comb[:])
            return
        for i in range(start, len(arr)):
            comb.append(arr[i])
            backtrack(i + 1, comb)
            comb.pop()
    result = []
    backtrack(0, [])
    return result

# Example usage
print(generate_combinations([1,2,3,4,5], 3))  # [[ generates the combination of 3 elements from the list [1,2,3,4,5] ]]
