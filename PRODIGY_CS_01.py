def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)

def main():
    choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (an integer): "))

    if choice == 'encrypt':
        result = caesar_cipher_encrypt(text, shift)
        print("Encrypted text:", result)
    elif choice == 'decrypt':
        result = caesar_cipher_decrypt(text, shift)
        print("Decrypted text:", result)

if __name__ == "__main__":
    main()
