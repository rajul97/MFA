# main.py

from otp_generator import generate_otp
from otp_verifier import verify_otp
from backup_codes import generate_backup_codes
from rate_limiter import RateLimiter
from logger import log_event
from config import RATE_LIMIT, RATE_LIMIT_WINDOW

def display_menu():
    print("\nMFA System Menu:")
    print("1. Generate OTP")
    print("2. Verify OTP")
    print("3. Show Backup Codes")
    print("4. Exit")

if __name__ == "__main__":
    # Initialize rate limiter and generate backup codes
    rate_limiter = RateLimiter(RATE_LIMIT, RATE_LIMIT_WINDOW)
    backup_codes = generate_backup_codes()

    print("Backup Codes (store these safely):")
    for code in backup_codes:
        print(code)
    
    print("\nWelcome to the MFA System!")

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            otp = generate_otp()
            print(f"Your OTP: {otp}")

        elif choice == "2":
            # Check rate limiter before allowing an attempt
            if not rate_limiter.is_allowed():
                print("Too many attempts. Please wait and try again.")
                log_event("User exceeded OTP verification rate limit", level="warning")
                continue

            user_code = input("Enter OTP: ")
            rate_limiter.add_attempt()  # Log this attempt
            if verify_otp(user_code):
                print("✅ OTP Verified! Access granted.")
                log_event("Successful OTP verification")
            else:
                print("❌ Incorrect OTP! Access denied.")
                log_event("Failed OTP verification", level="warning")

        elif choice == "3":
            print("Backup Codes (use these for account recovery):")
            for code in backup_codes:
                print(code)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice! Please select a valid option.")
