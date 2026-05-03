def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            print("Pattern found at index", i)

text = "AABAACAADAABAABA"
pattern = "AABA"

naive_search(text, pattern)