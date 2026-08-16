COMMON_PASSWORDS = [
    "123456", "password", "123456789", "12345678", "12345",
    "qwerty", "abc123", "password1", "111111", "iloveyou",
    "admin", "welcome", "letmein", "monkey", "dragon"
]

def check_strength(password):
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    
    score = sum([length_ok, has_upper, has_lower, has_digit, has_symbol])
    
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return {
        "length_ok": length_ok,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "strength": strength
    }

def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS

password = "Password123"

result = check_strength(password)
common = is_common_password(password)

print(f"Password: {password}")
for check, passed in result.items():
    print(f"{check}: {passed}")

if common:
    print("⚠️ WARNING: This password appears in a common/leaked password list!")
else:
    print("Not found in common password list.")
