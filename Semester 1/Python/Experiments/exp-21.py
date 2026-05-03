def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 'decrypt':
                shift = -shift
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        content = file.read()
    encrypted_content = caesar_cipher(content, shift, 'encrypt')
    with open(output_file, 'w') as file:
        file.write(encrypted_content)
    print(f"File encrypted: {output_file}")

def decrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        content = file.read()
    decrypted_content = caesar_cipher(content, shift, 'decrypt')
    with open(output_file, 'w') as file:
        file.write(decrypted_content)
    print(f"File decrypted: {output_file}")

# Example usage
if __name__ == "__main__":
    encrypt_file('plaintext.txt', 'encrypted.txt', 3)
    decrypt_file('encrypted.txt', 'decrypted.txt', 3)