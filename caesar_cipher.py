def caesar_encrypt(text, shift):
    """
    Encrypts the given text using Caesar cipher with the specified shift.
    Only letters are shifted; other characters remain unchanged.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Shift uppercase and lowercase letters separately
            base = ord('A') if char.isupper() else ord('a')
            # Shift and wrap-around using modulo
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def caesar_decrypt(cipher_text, shift):
    """
    Decrypts the given Caesar cipher text with the specified shift.
    """
    return caesar_encrypt(cipher_text, -shift)

if __name__ == "__main__":
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (integer): "))

    if choice == 'e':
        encrypted = caesar_encrypt(text, shift)
        print(f"Encrypted text: {encrypted}")
    elif choice == 'd':
        decrypted = caesar_decrypt(text, shift)
        print(f"Decrypted text: {decrypted}")
    else:
        print("Invalid choice. Please type 'e' or 'd'.")
