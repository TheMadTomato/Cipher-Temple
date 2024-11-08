#==============================CLASS===========================================#
#==============================================================================#
class PigCrypt:
    """
    Implements a Pig Latin-style obfuscation, adding a layer of salting by transforming
    each word. It moves the first character of each word to the end and appends "AY",
    making it compatible with other simple ciphers like Caesar or transposition.
    """

    #===============================INIT========================================#
    #==========================================================================#
    def __init__(self, message: str = ""):
        # Initialize instance variable
        self.message = message

    #============================SET MESSAGE===================================#
    #==========================================================================#
    def set_message(self, message: str):
        """
        Sets the message to be obfuscated.
        """
        self.message = message.upper()

    #=============================OBFUSCATION==================================#
    #==========================================================================#
    def pigcrypt_encrypt(self) -> str:
        """
        Obfuscates the message using Pig Latin-style transformation.
        - Moves the first letter of each word to the end and appends "AY."
        - Returns the obfuscated message.
        """
        words = self.message.split()
        encrypted_words = []
        
        for word in words:
            if len(word) > 1:
                encrypted_words.append(word[1:] + word[0] + "AY")
            else:
                encrypted_words.append(word + "AY")  # For single-character words

        return "".join(encrypted_words)

    #=============================DECRYPTION===================================#
    #==========================================================================#
    def pigcrypt_decrypt(self) -> str:
        """
        Decrypts the Pig Latin-style obfuscated message.
        - Removes "AY" from the end of each word and moves the last character
          back to the beginning.
        - Returns the decrypted message.
        """
        cipher = self.message.split('AY')
        decrypted_words = []

        for part in cipher:
            if part:  # Ensure it's not an empty string
                decrypted_word = part[-1] + part[:-1]
                decrypted_words.append(decrypted_word)
        
        return " ".join(decrypted_words)

