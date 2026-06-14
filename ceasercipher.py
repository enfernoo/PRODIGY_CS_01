def caesar_cipher(message, shift, mode):
    result = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            if mode == "encrypt":
                new_char = chr((ord(char) - start + shift) % 26 + start) # wrap around from a to z, z to a
            elif mode == "decrypt":
                new_char = chr((ord(char) - start - shift) % 26 + start)

            result += new_char
        else:
            result += char

    return result


# Taking input
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

choice = input("Do you want to encrypt or decrypt? ").lower()

if choice == "encrypt" or choice == "decrypt":
    output = caesar_cipher(message, shift, choice)
    print("Result:", output)
else:
    print("Invalid choice. Please enter encrypt or decrypt.")