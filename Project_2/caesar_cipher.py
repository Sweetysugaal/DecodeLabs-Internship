def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            encrypted_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            encrypted_text += encrypted_char

        elif char.islower():
            encrypted_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            encrypted_text += encrypted_char

        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter your message: ")
shift = int(input("Enter the shift key: "))

encrypted_message = encrypt(message, shift)
decrypted_message = decrypt(encrypted_message, shift)

print("\nEncrypted:", encrypted_message)
print("Decrypted:", decrypted_message)

if decrypted_message == message:
    print("Decryption successful!")
else:
    print("Decryption failed.")

    