import crypt

target_hash = "42hDRfypTqqnw"
salt = target_hash[:2]

with open("rockyou.txt") as f:
    for password in f:
        password = password.strip()
        if crypt.crypt(password, salt) == target_hash:
            print(f"Found: {password}")
            break
