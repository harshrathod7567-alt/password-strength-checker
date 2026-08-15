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

password = "Password123"  # try changing this to test different passwords
result = check_strength(password)

print(f"Password: {password}")
for check, passed in result.items():
    print(f"{check}: {passed}")
