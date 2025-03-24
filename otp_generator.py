# otp_generator.py

import pyotp
import qrcode
from config import SECRET_KEY, ISSUER_NAME, USERNAME

def generate_qr_code():
    """
    Generates a QR Code that can be scanned with an authenticator app.
    """
    totp = pyotp.TOTP(SECRET_KEY)
    uri = totp.provisioning_uri(name=USERNAME, issuer_name=ISSUER_NAME)
    qr = qrcode.make(uri)
    qr.save("qrcode.png")
    print("QR Code generated! Scan it using Google Authenticator or any MFA app.")

def generate_otp():
    """
    Generates the current OTP using TOTP.
    """
    totp = pyotp.TOTP(SECRET_KEY)
    return totp.now()

if __name__ == "__main__":
    generate_qr_code()
    print(f"Generated OTP: {generate_otp()}")
