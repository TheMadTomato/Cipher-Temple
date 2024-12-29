#=================================IMPORTS======================================#
#==============================================================================#
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

#==============================CLASS===========================================#
#==============================================================================#
class RSACipher:
    """
    Implements RSA encryption and decryption with support for generating keys.
    """

    #===============================INIT========================================#
    #==========================================================================#
    def __init__(self):
        # Generate RSA keys upon initialization
        self.key_pair = RSA.generate(2048)
        self.public_key = self.key_pair.publickey()
        self.private_key = self.key_pair

    #==========================GET PUBLIC KEY==================================#
    #==========================================================================#
    def get_public_key(self) -> str:
        """
        Returns the public key in PEM format.
        """
        return self.public_key.export_key().decode('utf-8')

    #==========================GET PRIVATE KEY=================================#
    #==========================================================================#
    def get_private_key(self) -> str:
        """
        Returns the private key in PEM format.
        """
        return self.private_key.export_key().decode('utf-8')

    #=============================ENCRYPT======================================#
    #==========================================================================#
    def encrypt(self, message: str) -> str:
        """
        Encrypts a message using the public key.
        - Returns the base64-encoded ciphertext.
        """
        cipher = PKCS1_OAEP.new(self.public_key)
        ciphertext = cipher.encrypt(message.encode('utf-8'))
        return base64.b64encode(ciphertext).decode('utf-8')

    #=============================DECRYPT======================================#
    #==========================================================================#
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a base64-encoded ciphertext using the private key.
        - Returns the original plaintext message.
        """
        cipher = PKCS1_OAEP.new(self.private_key)
        decrypted_data = cipher.decrypt(base64.b64decode(ciphertext))
        return decrypted_data.decode('utf-8')
