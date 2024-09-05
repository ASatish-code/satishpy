import itertools

# Define lists A, B, C, D, E
A = ['A1', 'A2', 'A3']
B = ['B1', 'B2']
C = ['C1', 'C2', 'C3', 'C4']
D = ['D1', 'D2', 'D3']
E = ['E1', 'E2']

# Create a combined list
combined_list = A + B + C + D + E

# Step 1: Compute all combinations (choosing 2 elements at a time, can adjust r-value)
print("Combinations (choosing 2 elements at a time):")
combinations = list(itertools.combinations(combined_list, 2))
for combo in combinations:
    print(combo)

# Step 2: Compute all permutations (arranging 2 elements at a time, can adjust r-value)
print("\nPermutations (arranging 2 elements at a time):")
permutations = list(itertools.permutations(combined_list, 2))
for perm in permutations:
    print(perm)

# Step 3: Compute combinations of the entire list (select any r value, here r = 3)
print("\nCombinations of 3 elements:")
combinations_3 = list(itertools.combinations(combined_list, 3))
for combo in combinations_3:
    print(combo)

# Step 4: Compute permutations of the entire list (select any r value, here r = 3)
print("\nPermutations of 3 elements:")
permutations_3 = list(itertools.permutations(combined_list, 3))
for perm in permutations_3:
    print(perm)
