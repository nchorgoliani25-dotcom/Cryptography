import base64

def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            decrypted += char
    return decrypted

# Part 1
ciphertext1 = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
print("Caesar Cipher Brute-force results:")
for shift in range(1, 26):
    print(f"Shift {shift}: {caesar_decrypt(ciphertext1, shift)}")

# Part 2: decrypt mznxpz -> get anagram 'rescue' -> passphrase 'secure'
cipher_m = "mznxpz"
print("\nCaesar brute-force for 'mznxpz':")
for shift in range(1, 26):
    print(shift, caesar_decrypt(cipher_m, shift))

# chosen passphrase (anagram): "secure"
passphrase = "secure"

# Part 3: XOR decryption
ciphertext_base64 = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
cipher_bytes = base64.b64decode(ciphertext_base64)

def xor_decrypt(data, key):
    key_bytes = key.encode()
    decrypted = bytearray()
    for i in range(len(data)):
        decrypted.append(data[i] ^ key_bytes[i % len(key_bytes)])
    return decrypted

plaintext_bytes = xor_decrypt(cipher_bytes, passphrase)
plaintext = plaintext_bytes.decode(errors='ignore')
print("\nXOR Decrypted Text:")
print(plaintext)
