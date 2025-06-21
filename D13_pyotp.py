'''
Day 13, June 18nd 2025: 

Welcome to pyotp!

Two-factor authentication made simple. Generate those
6-digit codes you see in Google Authenticator, protect
accounts with time-based tokens, and add security layers
to your apps. Fort Knox-level protection in 20 lines.
'''

import pyotp
import qrcode
import time

# Generate a secret key (keep this safe!)
secret = pyotp.random_base32()
print(f"🔑 Secret: {secret}")

# Create TOTP (Time-based One-Time Password) generator
totp = pyotp.TOTP(secret)

# Generate current 6-digit code
current_code = totp.now()
print(f"🔢 Current code: {current_code}")

# Verify a code (returns True/False)
is_valid = totp.verify(current_code)
print(f"✅ Code valid: {is_valid}")

# Generate QR code for authenticator apps
provisioning_uri = totp.provisioning_uri(
    name="user@example.com",
    issuer_name="My App"
)
qr = qrcode.make(provisioning_uri)
qr.save('totp_qr.png')
print("📱 QR code saved: totp_qr.png (scan with Google Authenticator)")

# Demo: Watch codes change every 30 seconds
print("\n⏰ Watching codes change:")
for i in range(3):
    print(f"Code: {totp.now()} (valid for {30 - int(time.time()) % 30}s)")
    time.sleep(10)