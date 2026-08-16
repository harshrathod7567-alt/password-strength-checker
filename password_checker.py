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

def write_report(password, result, common, output_file="password_report.txt"):
    with open(output_file, 'w') as f:
        f.write("=== Password Strength Report ===\n\n")
        f.write(f"Password checked: {'*' * len(password)} (hidden for safety)\n\n")
        for check, passed in result.items():
            f.write(f"{check}: {passed}\n")
        f.write("\n")
        if common:
            f.write("⚠️ WARNING: This password appears in a common/leaked password list!\n")
        else:
            f.write("Not found in common password list.\n")
    print(f"Report saved to {output_file}")

password = "Password123"

result = check_strength(password)
common = is_common_password(password)

print(f"Password: {password}")
for check, passed in result.items():
    print(f"{check}: {passed}")

write_report(password, result, common)
