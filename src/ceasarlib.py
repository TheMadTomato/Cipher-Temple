#=================================IMPORTS======================================#
#==============================================================================#
from getpass import getpass

#==============================CLASS===========================================#
#==============================================================================#
class CaesarCipher:
    """
    Implements Caesar Cipher encryption and decryption with support for handling
    integer and string-based keys. Key input is masked for security.
    """

    #===============================INIT========================================#
    #==========================================================================#
    def __init__(self, message: str = "", key: int = 0):
        # Initialize instance variables
        self.message = message
        self.key = key

    #============================SET MESSAGE===================================#
    #==========================================================================#
    def set_message(self, message: str):
        """
        Sets the message to be encrypted or decrypted.
        """
        self.message = message

    #==============================SET KEY=====================================#
    #==========================================================================#
    def set_key(self, key: int):
        """
        Sets the encryption/decryption key.
        - Accepts an integer key for shifting characters.
        """
        if isinstance(key, int):
            self.key = key
        else:
            raise ValueError("Key must be an integer")

    #=============================ENCRYPTION===================================#
    #==========================================================================#
    def caesar_encrypt(self) -> str:
        """
        Encrypts the message using the Caesar cipher.
        - Shifts alphabetical characters by the key, skipping spaces and numbers.
        - Returns the encrypted message.
        """
        result = []
        for char in self.message:
            if char.isalpha():  # Encrypt only alphabetic characters
                # Shift character based on ASCII value
                shift = (ord(char.upper()) - 65 + self.key) % 26 + 65
                result.append(chr(shift))
        return ''.join(result)

    #=============================DECRYPTION===================================#
    #==========================================================================#
    def caesar_decrypt(self) -> str:
        """
        Decrypts the message using the Caesar cipher.
        - Shifts characters back by the key value.
        - Returns the decrypted message.
        """
        result = []
        for char in self.message:
            if char.isalpha():  # Decrypt only alphabetic characters
                shift = (ord(char.upper()) - 65 - self.key) % 26 + 65
                result.append(chr(shift))
        return ''.join(result)

    #==============================GET KEY=====================================#
    #==========================================================================#
    def get_key_from_user(self):
        """
        Prompts the user to enter a key, which can be an integer or a string.
        - Integer values are directly used as the key.
        - String values are converted to their length to be used as the key.
        - Hides input for security.
        """
        while True:
            input_key = getpass("Enter Key: ")
            try:
                key = int(input_key)  # Attempt to use input as an integer
                self.set_key(key)
                break
            except ValueError:
                # If not an integer, use the length of the input string as the key
                key = len(input_key)
                self.set_key(key)
                break

