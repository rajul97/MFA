# config.py

# MFA configuration settings
SECRET_KEY = "NeuralNineMySuperSecretKey"
ISSUER_NAME = "Rajulgupta App"
USERNAME = "Rajul"

# OTP verification tolerance (allows one time-step before/after current)
VALID_WINDOW = 1

# Rate limiter settings (max attempts per window)
RATE_LIMIT = 5            # Maximum allowed attempts
RATE_LIMIT_WINDOW = 60    # Window in seconds (e.g., 60 seconds)
