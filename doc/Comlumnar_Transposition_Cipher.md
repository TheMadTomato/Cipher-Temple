# Columnar Transposition Cipher
The Columnar Transposition Cipher is a Classical, Polyalphabetic cipher that rearranges characters in a message based on a key. The key dictates the column order, and the message is transposed row by row into a matrix based on this key length. Padding can be applied if needed to complete the matrix. This method provides a simple form of obfuscation.

***NOTE***
The Function here is a little bit different than the main code because here is the version of the function outside of a class for direct use.

## Columnar Transposition Encrypt Function
The `coltranspo_encrypt` function performs encryption using the Columnar Transposition Cipher. It takes two parameters: `message` (the text to be encrypted) and `key` (the string used to determine column order). Here’s a breakdown of the process:
```python
def coltranspo_encrypt(message:str, key:str) -> str:

    # Initialize Variables
    ## Slice the Message into a List & Return Lenght of Message as Float in Case 
    ## Padding is needed
    m_list = list(message)
    m_len = float(len(message))

    ## Slice and Sort Key in Alphabetcal order
    k_list = sorted(list(key))
    k_len = len(key)

    ## To Parse Through the Matrix based on `k_list`
    k_index = 0

    ## Placeholder for the ecnrypted text
    ciphertext = ""

    # Initialize Row & Col for the Matrix Table
    col = len(key)
    row = int(ceil(m_len / col))

    # If Message Length is ODD Padd it Until it Becomes Even 
    if is_odd(m_len):
        padding_char = get_padding_char()
        padding_num = int((row * col) - m_len)
        m_list.extend(padding_char * padding_num)

    # Create Matrix and Insert Message and Padding Character if Included 
    matrix = [m_list[i: i + col]
              for i in range(0, len(m_list), col)]

    # Read Matrix Column Wise Based on the Sorted Key and Write it Down 
    for _ in range(col):
        current_i = key.index(k_list[k_index])
        ciphertext += ''.join([row[current_i]
                              for row in matrix])
        k_index += 1

    return ciphertext
```

1. **Initialization**: 
   - The function starts by converting the `message` into a list of characters (`m_list`) and storing its length as a float (`m_len`). This allows for calculations involving padding if the message length doesn’t fit perfectly within the columns.
   - The `key` is also converted into a sorted list of characters (`k_list`), allowing the function to read columns in alphabetical order as dictated by the `key`.

2. **Matrix Dimensions**:
   - The function calculates the number of columns (`col`) based on the key length, and the number of rows (`row`) by dividing the message length by the number of columns and rounding up using `ceil`.

3. **Padding**:
   - If the message length is odd and padding is needed to complete the matrix, the function calls `get_padding_char()` to ask for a single padding character.
   - The function appends enough of this padding character to make the message length a multiple of the number of columns.

4. **Matrix Creation**:
   - A matrix is created from `m_list`, with each row containing a number of characters equal to the key length. This matrix represents the layout of the message text within the grid.

5. **Column-Wise Reading for Encryption**:
   - The function constructs the `ciphertext` by reading characters column-wise. For each column (in the order defined by `k_list`), it retrieves the corresponding characters from each row and appends them to `ciphertext`.

6. **Output**:
   - Finally, `ciphertext`, which now contains the encrypted message, is returned as a single concatenated string.

## Columnar Transposition Decrypt Function 
The `coltranspo_decrypt` function performs decryption using the Columnar Transposition Cipher. It takes two parameters: `ciphertext` (the encrypted text) and `key` (the string used to determine the column order). Here’s a breakdown of the decryption process:
```python
def coltranspo_decrypt(ciphertext: str, key: str) -> str:
    
    # Initialize Variables
    c_len = float(len(ciphertext))
    c_list = list(ciphertext)
    c_index = 0

    k_list = sorted(list(key))
    k_index = 0

    message = ""

    # Initialize Matrix 
    col = len(key)
    row = int(ceil(c_len / col))

    ## Create the Matrix 
    decrypted_cipher = []
    for _ in range(row):
        decrypted_cipher += [[None] * col]

    ## Fill Matrix 
    for _ in range(col):
        current_i = key.index(k_list[k_index])

        for j in range(row):
            decrypted_cipher[j][current_i] = c_list[c_index]
            c_index += 1
        k_index += 1

    # convert matrix into string
    try: 
        message = ''.join(sum(decrypted_cipher, []))
    except TypeError:
        raise TypeError("This Program Cannot Handle Repating Words.")
    
    # Remove padding Character
    # padd_count = message.count(padding_char)
    # if padd_count > 0: 
    #     return message[: -padd_count]
    return message
```

1. **Initialization**:
   - The function begins by converting `ciphertext` into a list of characters (`c_list`) and storing its length as a float (`c_len`). This helps in calculating the dimensions of the matrix.
   - The `key` is sorted alphabetically (`k_list`) to guide the order of reading columns in the decryption process.

2. **Matrix Dimensions**:
   - The number of columns (`col`) is determined by the length of the key, and the number of rows (`row`) is calculated by dividing `c_len` by the number of columns and rounding up using `ceil`.

3. **Matrix Creation**:
   - A matrix, `decrypted_cipher`, is initialized as a 2D list where each sublist represents a row in the matrix. The function fills this matrix column-by-column to recreate the message layout.

4. **Column-Wise Filling for Decryption**:
   - Using the sorted `k_list`, the function places each character from `c_list` into the appropriate matrix column as defined by the order of characters in `key`. For each column in sorted key order, characters are distributed across rows in the original sequence.

5. **Reconstructing the Message**:
   - After filling the matrix, the function flattens it row-by-row into a single string (`message`). This reorders the characters according to the original message before encryption.
   - The function attempts to join all elements into `message`. If the structure contains unintended duplicates, it raises a `TypeError` to signal an error in handling repeating words.

6. **Output**:
   - Finally, the decrypted message, `message`, is returned. The code includes a commented-out section that could remove padding characters if they were appended during encryption, ensuring that the output message matches the original plaintext exactly.


## Functions to Process Keys, Spaces, and Padding Character 
These 3 Functions are used to Process the necessary element to perform this algorithm.
### Remove Space Function
```python
def remove_space(plaintext: str) -> str:
    message = []
    for char in plaintext:
        if char.isalnum():
            message.append(char.upper())
    return ''.join(message)
```

The `remove_space` function is a helper method that formats the input message by removing any non-alphanumeric characters and converting all remaining characters to uppercase.

- **Purpose**: Ensures that only letters and numbers are retained in the message, making it suitable for the encryption process.
- **Process**:
  - Loops through each character in `plaintext`.
  - If the character is alphanumeric (`char.isalnum()`), it is converted to uppercase and appended to `message`.
  - Finally, `message` is joined into a single string and returned.
- **Return**: Returns a cleaned, uppercase version of the original text with spaces and special characters removed.

---

### Get Key Function
```python
def get_key() -> str:
    while True:
        try:
            key = input("Enter Key: ")
            if (len(key) == len(set(key))) and key.isalpha():
                return key.upper()
            else:
                raise ValueError("BadKey_Error: Duplicated or Non-Alphabetic Characters Spotted!")
        except ValueError as e:
            print(e)
```

The `get_key` function securely obtains and validates an encryption key from the user.

- **Purpose**: Ensures that the encryption/decryption key is unique and alphabetic, as required by the Columnar Transposition Cipher.
- **Validation**:
  - Checks that the key has no duplicate characters (`len(key) == len(set(key))`), meaning each character is unique.
  - Ensures that all characters are alphabetic (`key.isalpha()`).
  - If either condition is not met, a `ValueError` is raised with a descriptive error message.
- **Return**: If valid, the function returns the key in uppercase format.

---

### Get Padding Character Function
```python
def get_padding_char() -> str:
    while True:
        try:
            char = input("Enter Padding Character: ")
            if char.isalpha() and len(char) == 1:
                return char.upper()
            else:
                raise ValueError("BadPaddingChar_Error: Only One Alphabetic Character is Allowed")
        except ValueError as e:
            print(e)
```

The `get_padding_char` function prompts the user to input a padding character, validating that it is a single alphabetic character.

- **Purpose**: Ensures the padding character used for filling incomplete rows in the encryption matrix is a single valid letter.
- **Validation**:
  - Checks if the character is alphabetic (`char.isalpha()`) and that it is exactly one character in length (`len(char) == 1`).
  - If these conditions are not met, a `ValueError` is raised, and the user is prompted again.
- **Return**: Once validated, the function returns the padding character in uppercase.


