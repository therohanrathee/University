def is_palindrome(string):
    char_count = {}
    for char in string.lower():
        char_count[char] = char_count.get(char, 0) + 1
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    return odd_count <= 1

# Test the function with a sample string
input_string = "nitin"

result = is_palindrome(input_string)

print(f"\nInput String: {input_string}")
print(f"Can '{input_string}' be permuted to form a palindrome? {result}\n")