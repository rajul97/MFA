# backup_codes.py

import random
import string

def generate_backup_codes(n=5, length=8):
    """
    Generates a list of one-time backup codes.
    """
    codes = []
    for _ in range(n):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        codes.append(code)
    return codes

if __name__ == "__main__":
    codes = generate_backup_codes()
    print("Backup Codes:")
    for code in codes:
        print(code)
