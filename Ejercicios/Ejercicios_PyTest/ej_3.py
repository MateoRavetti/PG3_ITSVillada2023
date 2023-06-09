def is_anagram(word1, word2):
    
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    
    if len(word1) != len(word2):
        return False

  
    char_count = {}
    for char in word1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in word2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        else:
            return False

   
    return len(char_count) == 0
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))  # False
print(is_anagram("rail safety", "fairy tales"))  # True
print(is_anagram("python", "typhon"))  # True
print(is_anagram("openai", "aiopen"))  # True
