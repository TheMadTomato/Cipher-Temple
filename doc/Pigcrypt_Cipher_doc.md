# Pigcrypt Cipher

Pigcrypt is a **non-standard obfuscation technique** that can add a layer of security to strings. Although not a formal cipher, it changes the position of the first character in each word by moving it to the end of the word and appending the letters "ay." In a way, this technique is similar to the Pig Latin word game, and it can serve as a lightweight "salting" technique when combined with other simple ciphers such as Caesar or transposition ciphers.

Here is the explanation of each function in the `pigcryptlib` library:

### Pigcrypt Encrypt Function
```python
def pigcrypt_encrypt(message: str) -> str:
    message = message.split()
    for i in range(len(message)):
        message[i] = message[i][1:] + message[i][0] + "ay"
    return "".join(message)
```

This function takes a `message` string as an argument and applies the Pigcrypt transformation to it. 

- **message**: The plaintext string or sentence to be obfuscated.

**Explanation**:
- The input message is first split into individual words.
- For each word, the first letter is moved to the end, and "ay" is added as a suffix.
- The resulting transformed words are concatenated back into a single string without spaces.

### Pigcrypt Decrypt Function
```python
def pigcrypt_decrypt(cipher: str) -> str:
    cipher = cipher.split('ay')
    decrypted_words = []
    for part in cipher:
        if part:  # Ensure it's not an empty string
            decrypted_word = part[-1] + part[:-1]  # Move the last character to the front
            decrypted_words.append(decrypted_word)
    return " ".join(decrypted_words)
```

This function takes a `cipher` string, which has been encrypted using the Pigcrypt method, and reverses the process.

- **cipher**: The Pigcrypt-obfuscated string to be decrypted.

**Explanation**:
- The input string is split using "ay" as the delimiter.
- For each resulting segment, the last letter is moved back to the front to reverse the transformation.
- The decrypted words are joined back together with spaces to restore the original message.
