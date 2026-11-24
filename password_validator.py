import re

def validate_password(password, min_length=8):
    errors = []

    checks = [
        (len(password) >= min_length, f"Minimum {min_length} characters required."),
        (re.search(r"[A-Z]", password), "At least one uppercase letter required."),
        (re.search(r"[a-z]", password), "At least one lowercase letter required."),
        (re.search(r"\d", password), "At least one digit required."),
        (re.search(r"[^A-Za-z0-9]", password), "At least one special character required."),
        (not re.search(r"\s", password), "No whitespace allowed.")
    ]

    for valid, message in checks:
        if not valid:
            errors.append(message)

    return len(errors) == 0, errors


def validate_password_single_regex(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9])\S{8,}$"
    return bool(re.match(pattern, password))


if __name__ == "__main__":
    passwords = ["Secure@123", "weakpass", "NoSpecial123",
                 "nouppercase@123", "NoDigit@Pass"]

    for pwd in passwords:
        valid, errors = validate_password(pwd)
        print(f"\n{pwd}: {valid}")
        print("Single Regex:", validate_password_single_regex(pwd))
        for error in errors:
            print("-", error)