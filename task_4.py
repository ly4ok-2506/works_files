def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            code = ord(char)
            if 'А' <= char <= 'Я' or 'а' <= char <= 'я':
                if char.isupper():
                    result += chr((code - 1040 + shift) % 32 + 1040)
                else:
                    result += chr((code - 1072 + shift) % 32 + 1072)
            elif 'A' <= char <= 'Z' or 'a' <= char <= 'z':
                if char.isupper():
                    result += chr((code - 65 + shift) % 26 + 65)
                else:
                    result += chr((code - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

with open('resource/secret.txt', 'r', encoding='utf-8') as f:
    text = f.read()

encrypted = encrypt(text, 3)
with open('encrypted.txt', 'w', encoding='utf-8') as f:
    f.write(encrypted)

decrypted = encrypt(encrypted, -3)
with open('decrypted.txt', 'w', encoding='utf-8') as f:
    f.write(decrypted)

print("Готово!")