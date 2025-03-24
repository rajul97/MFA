# rate_limiter.py

import time

class RateLimiter:
    """
    Simple rate limiter to restrict the number of attempts within a time window.
    """
    def __init__(self, max_attempts, window_seconds):
        self.max_attempts = max_attempts
        self.window_seconds = window_seconds
        self.attempts = []

    def add_attempt(self):
        now = time.time()
        self.attempts.append(now)
        self.clean_attempts(now)

    def clean_attempts(self, now):
        self.attempts = [t for t in self.attempts if now - t <= self.window_seconds]

    def is_allowed(self):
        now = time.time()
        self.clean_attempts(now)
        return len(self.attempts) < self.max_attempts

# For testing, you can run this file directly.
if __name__ == "__main__":
    limiter = RateLimiter(3, 10)
    for i in range(5):
        if limiter.is_allowed():
            print("Attempt allowed")
            limiter.add_attempt()
        else:
            print("Too many attempts!")
        time.sleep(2)
