#==============================iMPORTS=========================================#
#==============================================================================#
from ceasarlib import CaesarCipher
from collections import Counter

#==============================CLASS===========================================#
#==============================================================================#
class CaesarAttack:
    """
    Implements a brute force attack on Caesar Cipher to identify the most probable key.
    Includes an additional method to display all possible decrypted texts.
    """

    #===============================INIT========================================#
    #==========================================================================#
    def __init__(self, ciphertext: str):
        # Initialize instance variable
        self.ciphertext = ciphertext

    #============================BRUTE FORCE ATTACK============================#
    #==========================================================================#
    def brute_force_attack(self) -> tuple:
        """
        Performs a brute force attack to decrypt the Caesar cipher.
        - Evaluates all possible key combinations (0-25).
        - Returns the most probable key and the corresponding plaintext.
        """
        probable_key = None
        probable_plaintext = None
        max_score = -1

        for key in range(26):
            # Decrypt with current key
            cipher = CaesarCipher(self.ciphertext, key)
            decrypted_text = cipher.caesar_decrypt()

            # Analyze decrypted text using frequency analysis
            score = self._evaluate_text(decrypted_text)

            if score > max_score:
                max_score = score
                probable_key = key
                probable_plaintext = decrypted_text

        return probable_key, probable_plaintext

    #========================SHOW ALL POSSIBLE TEXTS===========================#
    #==========================================================================#
    def show_all_possible_texts(self) -> None:
        """
        Displays all possible decrypted texts along with their corresponding keys.
        Highlights the most probable text.
        """
        probable_key = None
        probable_plaintext = None
        max_score = -1

        print("\nAll Possible Decrypted Texts:")
        for key in range(26):
            # Decrypt with current key
            cipher = CaesarCipher(self.ciphertext, key)
            decrypted_text = cipher.caesar_decrypt()

            # Analyze decrypted text using frequency analysis
            score = self._evaluate_text(decrypted_text)
            print(f"Key {key:02}: {decrypted_text}")

            if score > max_score:
                max_score = score
                probable_key = key
                probable_plaintext = decrypted_text

        print("\nMost Probable Decrypted Text:")
        print(f"Key {probable_key:02}: {probable_plaintext}")

    #============================TEXT EVALUATION===============================#
    #==========================================================================#
    def _evaluate_text(self, text: str) -> float:
        """
        Evaluates the decrypted text based on letter frequency analysis.
        - Uses statistical frequency of letters in English.
        """
        # Frequency of letters in the English language
        letter_frequencies = {
            'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
            'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
            'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
            'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'X': 0.15, 'J': 0.10,
            'Q': 0.10, 'Z': 0.07
        }

        # Calculate score based on frequency analysis
        score = 0
        for char in text.upper():
            if char in letter_frequencies:
                score += letter_frequencies[char]
            else:
                # Penalize non-alphabetic characters
                score -= 5

        return score
