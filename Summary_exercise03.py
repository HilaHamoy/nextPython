import string


# הגדרת חריגות מותאמות אישית
class UsernameContainsIllegalCharacter(Exception):
    pass


class UsernameTooShort(Exception):
    pass


class UsernameTooLong(Exception):
    pass


class PasswordMissingCharacter(Exception):
    pass


class PasswordTooShort(Exception):
    pass


class PasswordTooLong(Exception):
    pass


def check_input(username, password):
    legal_chars = set(string.ascii_letters + string.digits + '_')

    # בדיקת שם המשתמש
    if not (3 <= len(username) <= 16):
        if len(username) < 3:
            raise UsernameTooShort("the username is too short")
        else:
            raise UsernameTooLong("the username is too long")

    if any(char not in legal_chars for char in username):
        raise UsernameContainsIllegalCharacter("The username contains an illegal character")

    # בדיקת הסיסמה
    if not (8 <= len(password) <= 40):
        if len(password) < 8:
            raise PasswordTooShort("the Password is too short")
        else:
            raise PasswordTooLong("the Password is too long")

    has_upper = any(char in string.ascii_uppercase for char in password)
    has_lower = any(char in string.ascii_lowercase for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if not (has_upper and has_lower and has_digit and has_special):
        raise PasswordMissingCharacter("The password is missing a character")

    # אם כל הבדיקות עברו בהצלחה
    print("OK")


# דוגמאות לשימוש בפונקציה
try:
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")
except Exception as e:
    print(e)


