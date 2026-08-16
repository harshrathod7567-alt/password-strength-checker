# Password Strength Checker

A beginner Python project that evaluates password strength based on character 
composition rules and checks against a list of commonly leaked/weak passwords.

## What it does
- Checks length (8+ characters), uppercase, lowercase, digits, and symbols
- Scores the password as Weak, Medium, or Strong
- Flags passwords that match a list of known common/leaked passwords
- Saves results to a report file (with the password masked for safety)

## Files
- `password_checker.py` — the main script

## How to run it
1. Open `password_checker.py` and change the `password` variable to test different passwords
2. Run: `python password_checker.py`
3. Check the terminal output and `password_report.txt` for results

## Example output
Password: Password123
length_ok: True
has_upper: True
has_lower: True
has_digit: True
has_symbol: False
strength: Medium
Not found in common password list.

## What I learned
- How password strength policies work in practice
- Why "looks strong" passwords can still be dangerous if leaked/reused
- Basic security hygiene: never log sensitive data (like passwords) in plain text

## Next steps
- Load a much larger leaked-password list (e.g., rockyou.txt) for realistic checking
- Add a simple hash-cracking demo showing how weak passwords fall to dictionary attacks
- Build a simple web/CLI interface for interactive checking
