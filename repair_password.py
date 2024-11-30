from werkzeug.security import generate_password_hash
passowrd = input("Enter Password to repair: ")
hash_and_salted_password = generate_password_hash(
            passowrd,
            method='pbkdf2:sha256',
            salt_length=8
        )
print(hash_and_salted_password)