#=================================IMPORTS======================================#
#==============================================================================#
from math import ceil
from getpass import getpass

#=================================CLASS========================================#
#==============================================================================#
class ColumnarTranspositionCipher:
    """
    Implements a Columnar Transposition Cipher with support for encryption,
    decryption, and customizable padding.
    """

    #===============================INIT=======================================#
    #==========================================================================#
    def __init__(self, message: str = "", key: str = "", padding_char: str = ""):
        # Initialize instance variables
        self.message = message
        self.key = key
        self.padding_char = padding_char

    #============================SET MESSAGE===================================#
    #==========================================================================#
    def set_message(self, message: str):
        """
        Sets and formats the message to be encrypted or decrypted.
        - Removes any non-alphanumeric characters and converts to uppercase.
        """
        self.message = self.remove_space(message)

    #==============================SET KEY=====================================#
    #==========================================================================#
    def set_key(self, key: str):
        """
        Sets and validates the encryption/decryption key.
        - Ensures key is alphabetic and contains unique characters only.
        """
        if len(key) == len(set(key)) and key.isalpha():
            self.key = key.upper()
        else:
            raise ValueError("Key must be unique and alphabetic")

    #=========================SET PADDING CHAR=================================#
    #==========================================================================#
    def set_padding_char(self, char: str):
        """
        Sets and validates the padding character.
        - Ensures the character is a single alphabetic letter.
        """
        if char.isalpha() and len(char) == 1:
            self.padding_char = char.upper()
        else:
            raise ValueError("Padding character must be a single alphabetic character")

    #============================ENCRYPTION====================================#
    #==========================================================================#
    def coltranspo_encrypt(self) -> str:
        """
        Encrypts the message using columnar transposition with the set key.
        - Pads the message if necessary, requesting padding character from user.
        - Returns the encrypted ciphertext.
        """
        if not self.key:
            raise ValueError("Encryption key is not set")
        
        # Initialize Variables
        m_list = list(self.message)
        m_len = float(len(self.message))
        k_list = sorted(list(self.key))
        k_index = 0
        ciphertext = ""
        
        # Calculate Matrix Rows and Columns
        col = len(self.key)
        row = int(ceil(m_len / col))
        
        # Pad Message if Necessary
        if m_len % col != 0:
            if not self.padding_char:  # Request padding character if not already set
                self.set_padding_char(input("Enter Padding Character: "))
            padding_num = int((row * col) - m_len)
            m_list.extend(self.padding_char * padding_num)
        
        # Create Matrix and Fill with Message (Including Padding)
        matrix = [m_list[i: i + col] for i in range(0, len(m_list), col)]
        
        # Read Matrix by Columns in Sorted Key Order
        for _ in range(col):
            current_i = self.key.index(k_list[k_index])
            ciphertext += ''.join([row[current_i] for row in matrix])
            k_index += 1

        return ciphertext
    
    #============================DECRYPTION====================================#
    #==========================================================================#
    def coltranspo_decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the given ciphertext using the columnar transposition method
        with the set key.
        - Returns the decrypted message.
        """
        if not self.key:
            raise ValueError("Decryption key is not set")
        
        # Initialize Variables
        c_len = float(len(ciphertext))
        c_list = list(ciphertext)
        k_list = sorted(list(self.key))
        k_index = 0
        message = ""
        
        # Calculate Matrix Rows and Columns
        col = len(self.key)
        row = int(ceil(c_len / col))
        
        # Initialize Decryption Matrix
        decrypted_cipher = [[None] * col for _ in range(row)]
        
        # Fill Matrix by Columns in Sorted Key Order
        c_index = 0
        for _ in range(col):
            current_i = self.key.index(k_list[k_index])
            for j in range(row):
                decrypted_cipher[j][current_i] = c_list[c_index]
                c_index += 1
            k_index += 1
        
        # Flatten Matrix to String for Decrypted Message
        try:
            message = ''.join(sum(decrypted_cipher, []))
        except TypeError:
            raise TypeError("Cannot handle repeating words.")
        
        return message
    
    #============================REMOVE SPACE==================================#
    #==========================================================================#
    def remove_space(self, text: str) -> str:
        """
        Helper function to remove non-alphanumeric characters from text.
        - Converts text to uppercase.
        - Returns formatted text.
        """
        return ''.join(char.upper() for char in text if char.isalnum())

