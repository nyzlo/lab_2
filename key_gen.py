from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()

    with open("secret_key", "wb") as key_file:
        key_file.write(key)
    print(f"Nyckel sparad som: secret_key")

if __name__ == "__main__":
    generate_key()