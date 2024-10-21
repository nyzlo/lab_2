import argparse
from cryptography.fernet import Fernet

def setup_key():
	try:
		with open("secret_key", "rb") as file:
			return file.read()

	except FileNotFoundError:
		print("[Error] Missing secret_key file. Run generate_key.py first.")

def encrypt(input_file):
		key = setup_key()
		if key is None:
			return

		cipher_suite = Fernet(key)

		try:
			with open(input_file, "rb") as file:
				file_data = file.read()

			encrypted_message = cipher_suite.encrypt(file_data)

			with open(f"{input_file}.encrypted", "wb") as file:
				file.write(encrypted_message)

			print(f"File {input_file} encrypted and saved as {input_file}.encrypted")

		except FileNotFoundError:
			print("[ERROR] Invalid file input: {input_file}")

def decrypt(input_file):
	key = setup_key()
	if key is None:
		return

	cipher_suite = Fernet(key)

	try:
		with open(input_file, "rb") as file:
			encrypted_message = file.read()

		decrypted_message = cipher_suite.decrypt(encrypted_message)

		og_filename = input_file.replace(".encrypted", "")

		with open(og_filename, "wb") as file:
			file.write(decrypted_message) 

		print(f"File {input_file} decrypted and saved as {og_filename}")

	except FileNotFoundError:
		print(f"[ERROR] Invalid file input: {input_file}")

	except Exception:
		print(f"[ERROR] Corrupted file or trying to decrypt a plain text file")

def main():
	parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using a symmetrical key(secret_key)")

	parser.add_argument("-e", metavar="file", help="Encrypt a target file")
	parser.add_argument("-d", metavar="file", help="Decrypt a target file")

	args = parser.parse_args()

	if args.e:
		encrypt(args.e)
	elif args.d:
		decrypt(args.d)

main()