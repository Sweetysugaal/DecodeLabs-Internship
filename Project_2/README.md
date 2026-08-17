# Project 2 — Basic Encryption & Decryption 🔐

## Overview

As part of my DecodeLabs Cyber Security Internship 2026, Project 2 focuses on fundamental cryptography concepts through the implementation of a Caesar cipher.

The project demonstrates how plaintext can be transformed into ciphertext using a shift key and then converted back to the original plaintext through decryption.

## Objectives

- Encrypt user-provided text using a Caesar cipher.
- Decrypt the encrypted text.
- Display both encrypted and decrypted output.
- Handle uppercase and lowercase characters.
- Preserve spaces and punctuation.
- Validate that the decrypted message matches the original message.

## Technologies Used

- Python
- Functions
- `for` loops
- Conditional statements
- `ord()`
- `chr()`
- Modular arithmetic
- String handling

## How It Works

The program uses a Caesar cipher where each letter is shifted by a user-provided key.

Encryption uses the concept:

E(x) = (x + n) % 26

Decryption reverses the shift:

D(x) = (x - n) % 26

The program uses `ord()` to convert characters into integer values and `chr()` to convert the resulting values back into characters.

## Example

Input:

```text
Message: Hello World!
Shift: 3

Output:

Encrypted: Khoor Zruog!
Decrypted: Hello World!
Decryption successful!

Security Note

The Caesar cipher is intended for educational purposes only. It is not suitable for protecting sensitive information because it has a very small key space and preserves patterns in the original language.

What I Learned

Through this project, I practiced:

Basic encryption and decryption concepts
Caesar cipher logic
Modular arithmetic
Character encoding with ord() and chr()
Python functions
Handling edge cases
Validating encryption/decryption results
Understanding the difference between educational cryptography and modern secure encryption
Project Status

Completed ✅