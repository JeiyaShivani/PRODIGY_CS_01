def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha(): 
            shift_base = 65 if char.isupper() else 97 
            #wrapping around the value within A to Z
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  
    return result

if __name__ == "__main__":
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Do you want to 'encrypt' or 'decrypt' the message? ").lower()

    if mode == 'encrypt':
        encrypted_message = caesar_cipher(text, shift, 'encrypt')
        print(f"Encrypted message: {encrypted_message}")
    elif mode == 'decrypt':
        decrypted_message = caesar_cipher(text, shift, 'decrypt')
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
