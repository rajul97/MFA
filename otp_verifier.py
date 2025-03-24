# otp_verifier.py

import pyotp
from config import SECRET_KEY, VALID_WINDOW

def verify_otp(input_code):
    """
    Verifies the user-entered OTP with a valid window for clock drift.
    """
    totp = pyotp.TOTP(SECRET_KEY)
    return totp.verify(input_code, valid_window=VALID_WINDOW)

if __name__ == "__main__":
    input_code = input("Enter the OTP: ")
    if verify_otp(input_code):
        print("✅ OTP is valid! Authentication successful.")
    else:
        print("❌ Invalid OTP! Please try again.")
