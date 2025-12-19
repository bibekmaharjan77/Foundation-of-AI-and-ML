'''
Design Ideas
- The sign of a permutation tells if it is even (+1) or odd (-1), based on number of inversions.

- Inversion: Happens when a larger number appears before a smaller one in the sequence.

- Counts the total number of inversions; sign is (-1)^(inversions).

 

Structure of the program:
Loop through every pair (i,j),i<j. If arr[i] > arr[j], increment inversions.

- If inversions is even: sign = +1
- If inversions is odd: sign = -1

Return (-1)^(inversions)

'''

# Just run the file by python3 question3.py


# Permutation sign calculator
def permutation_sign(perm):
    '''Compute the sign (+1 or -1) of a permutation given as a list.'''
    inversions = 0
    n = len(perm)
    for i in range(n):
        for j in range(i+1, n):
            if perm[i] > perm[j]:
                inversions += 1
    return 1 if inversions % 2 == 0 else -1

# Examples:
print(permutation_sign([1,2,3])) # +1
print(permutation_sign([2,1,3])) # -1
