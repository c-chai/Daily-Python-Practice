# Test out fuzzywuzzy

from fuzzywuzzy import fuzz

# Token sort ratio comparison
sort_ratio = fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
print(f"Token sort ratio: {sort_ratio}")
