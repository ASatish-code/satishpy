import itertools

# Define lists A, B, C, D, E
A = ['A1', 'A2', 'A3']
B = ['B1', 'B2']
C = ['C1', 'C2', 'C3', 'C4']
D = ['D1', 'D2', 'D3']
E = ['E1', 'E2']

# Function to compute permutations and combinations for a list
def compute_permutations_combinations(lst):
    print(f"\nList: {lst}")
    
    # Compute all combinations (choose 2 elements at a time, r=2)
    print("Combinations (choosing 2 elements):")
    combinations = list(itertools.combinations(lst, 2))
    for combo in combinations:
        print(combo)
    
    # Compute all permutations (arrange 2 elements at a time, r=2)
    print("Permutations (arranging 2 elements):")
    permutations = list(itertools.permutations(lst, 2))
    for perm in permutations:
        print(perm)

# Perform computations for each list
print("Combinations and Permutations for List A:")
compute_permutations_combinations(A)

print("\nCombinations and Permutations for List B:")
compute_permutations_combinations(B)

print("\nCombinations and Permutations for List C:")
compute_permutations_combinations(C)

print("\nCombinations and Permutations for List D:")
compute_permutations_combinations(D)

print("\nCombinations and Permutations for List E:")
compute_permutations_combinations(E)
