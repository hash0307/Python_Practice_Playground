from collections import Counter

def find_missing_words(original: str, modified: str):
    original_words = original.split()
    modified_words = modified.split()

    print(f"Original Words(after split): {original_words}")
    print(f"Modified Words(after split): {modified_words}")
    
    # Count occurrences of words in both strings
    original_count = Counter(original_words)
    modified_count = Counter(modified_words)
    print(f"Original Count: {original_count}, \nModified Count: {modified_count}")
    print(f"Original Count Type: {type(original_count)}, \nModified Count: {type(modified_count)}")

    # Find missing words by comparing counts
    missing_words = []
    for word in original_count:
        missing_count = original_count[word] - modified_count.get(word, 0)
        missing_words.extend([word] * missing_count)  # Add missing words based on count

    return missing_words

# Example usage:
original = "I love love programming in Python and Java love"
modified = "I love in Python love"

print(find_missing_words(original, modified))
