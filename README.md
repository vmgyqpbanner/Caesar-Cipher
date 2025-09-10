# Caesar Cipher Python Script

This repository provides a simple Python script to encrypt and decrypt text using the Caesar Cipher algorithm.

## Features

- **Encryption**: Shift letters in your text by a specified amount.
- **Decryption**: Reverse the shift to retrieve the original message.
- **Non-letter Characters**: All non-letter characters (digits, punctuation, spaces) are left unchanged.

## Usage

1. **Run the Script**

   ```bash
   python caesar_cipher.py
   ```

2. **Choose Mode**

   - Type `e` for encryption or `d` for decryption.

3. **Input Text and Shift**

   - Enter the text you wish to encrypt or decrypt.
   - Enter the shift value (an integer).

## Example

```
Type 'e' to encrypt or 'd' to decrypt: e
Enter the text: Hello, World!
Enter the shift value (integer): 3
Encrypted text: Khoor, Zruog!
```

## How it Works

- Each letter in the input is shifted down the alphabet by the specified number (`shift`). For example, with a shift of 3, `A` becomes `D`, `B` becomes `E`, and so on.
- Decryption uses the negative of the shift value to reverse the process.

## License

This project is open source and available under the [MIT License](LICENSE).
