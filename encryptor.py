from cryptography.fernet import Fernet

# Generate and save key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print(f" {filename} encrypted successfully as {filename}.enc")

# Decrypt the file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    output_file = filename.replace(".enc", ".dec")
    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted)
    print(f"{filename} decrypted successfully as {output_file}")

# User interface
def main():
    print("\n--- ADVANCED ENCRYPTION TOOL ---")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        generate_key()
        print(" Key generated and saved as secret.key")
    elif choice == '2':
        filename = input("Enter file name to encrypt: ")
        encrypt_file(filename)
    elif choice == '3':
        filename = input("Enter encrypted file name (with .enc): ")
        decrypt_file(filename)
    elif choice == '4':
        print("Exiting...")
    else:
        print(" Invalid option")

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to perform another operation? (y/n): ")
        if again.lower() != 'y':
            break

