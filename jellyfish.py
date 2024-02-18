# Write code to see how to use the jellyfish module 

import jellyfish

# Example 1: Levenshtein Distance
distance = jellyfish.levenshtein_distance("jellyfish", "smellyfish")
print(f"Levenshtein distance between 'jellyfish' and 'smellyfish': {distance}")

# Example 2: Soundex
soundex_code = jellyfish.soundex("example")
print(f"Soundex code for 'example': {soundex_code}")

# Example 3: Metaphone
metaphone_code = jellyfish.metaphone("connection")
print(f"Metaphone code for 'connection': {metaphone_code}")

# Example 4: Match Rating Approach
match_rating = jellyfish.match_rating_codex("Robert")
print(f"Match Rating Approach codex for 'Robert': {match_rating}")

