def count_substring_occurrences(string, substring):
   
    if not string or not substring:
        return 0
    
    n = len(string)
    m = len(substring)
    
    # If the substring is longer than the string, it cannot appear
    if m > n:
        return 0
    
    count = 0
    
    # Iterate over the string using a sliding window
    for i in range(n - m + 1):
        # Check if the substring matches the current window
        if string[i:i + m] == substring:
            count += 1
    
    return count

# Example usage
main_string = "abcabcabc"
sub_string = "abc"
print(count_substring_occurrences(main_string, sub_string))  # Output: 3
