from Crypto.Cipher import AES
import base64
import itertools
import string

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text

encrypted_message = "OgJuOYJZT0FDb47DBOkNgA=="
partial_key = "IsASecretKey"

characters = string.ascii_letters
combinations = itertools.product(characters, repeat=4)

for combo in combinations:
    key = ''.join(combo) + partial_key
    try:
        decrypted_message = decrypt(encrypted_message, key)
        print(f"Chiave trovata: {key} | Messaggio decifrato: {decrypted_message}")
    except Exception as e:
        continue
