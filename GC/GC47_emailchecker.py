while True:
    def validate_email():
        email = input("Enter your email:")

        try:
            personal_info, domain_name = email.split('@')
        except ValueError:
            return "Invalid email: Missing '@' symbol"

        if len(email) > (64 + 1 + 253):
            return "Invalid email: Too long"

        if len(personal_info) > 64 or len(domain_name) > 253:
            return "Invalid email: Personal info or domain name part is too long"

        valid_chars_personal_info = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                        "abcdefghijklmnopqrstuvwxyz"
                                        "0123456789"
                                        "!#$%&'*+-/=?^_`{|}~")
        if not set(personal_info).issubset(valid_chars_personal_info):
            return "Invalid email: Personal info contains invalid characters"

        valid_chars_domain = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                 "abcdefghijklmnopqrstuvwxyz"
                                 "0123456789-.")
        if not set(domain_name).issubset(valid_chars_domain):
            return "Invalid email: Domain name contains invalid characters"

        if '..' in domain_name or domain_name.startswith('.') or domain_name.endswith('.'):
            return "Invalid email: Domain name has consecutive dots or starts/ends with a dot"

        return "Valid email"


    print(validate_email())
