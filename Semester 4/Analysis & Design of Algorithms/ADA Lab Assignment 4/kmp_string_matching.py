def compute_lps(pattern):
    lps = [0]*len(pattern)
    j = 0
    
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    
    return lps

def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    j = 0
    
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j-1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == len(pattern):
            print("Pattern found at index", i-j+1)
            j = lps[j-1]

text = "AAACAAAAAC"
pattern = "AAAA"

kmp_search(text, pattern)