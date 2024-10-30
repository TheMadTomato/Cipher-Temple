'''
Pigcrypt can be hardly considered a cipher, but it adds a layer of obfuscation on strings by changing the position of the first character in each word
to the end of the word and add the letters "ay" at its end. In a way it can be considered as a layer of salting to the original string and can prove to be useful
with other simple ciphers such as ceasar or transposition.

M = go study u lazy idiot
C = ogay tudysay uay azylay diotiay
  = ogaytudysayuayazylaydiotiay
'''

def pigcrypt_encrypt(message: str) -> str:
    # Split the message into words
    message = message.split()
    
    # For each word, move the first character to the end and add "ay"
    for i in range(len(message)):
        message[i] = message[i][1:] + message[i][0] + "AY"
    
    # Join the words without spaces
    return "".join(message)

def pigcrypt_decrypt(cipher: str) -> str:
    # Split the cipher text into words
    cipher = cipher.split('AY')
    
    # For each "word", move the last character (before "ay") back to the front
    decrypted_words = []
    for part in cipher:
        if part:  # Ensure it's not an empty string
            decrypted_word = part[-1] + part[:-1]  # Move the last character to the front
            decrypted_words.append(decrypted_word)
    
    # Join the decrypted words into a message
    return " ".join(decrypted_words)
