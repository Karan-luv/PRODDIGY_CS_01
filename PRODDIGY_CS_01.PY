def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift  

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  
    return result


text = input("Enter text: ")
shift = int(input("Enter shift value: "))
mode = input("Encrypt or Decrypt? ").strip().lower()

if mode in ["encrypt", "decrypt"]:
    output = caesar_cipher(text, shift, mode)
    print(f"Result: {output}")
else:
    print("Invalid mode! Choose either 'encrypt' or 'decrypt'.")
