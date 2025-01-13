import hashlib

# Get the MD5 hash from the user as an input
pass_hash = input("Enter md5 hash: ")

# Specify the wordlist file here we used 1.k most common passwords on the internet.
wordlist = "10k-most-common.txt"

# Here we try to open the wordlist file
try:
    pass_file = open(wordlist, "r")
except FileNotFoundError:
    print("No file found")
    quit()

# Used flag to check if password is found
flag = 0

# Iterate through each word in the wordlist
for word in pass_file:
    enc_wrd = word.encode("utf-8")
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()  # Corrected variable name

    # Check if the computed hash matches the provided hash
    if digest == pass_hash:
        print("Password found")
        print("Password is: " + word.strip())  # Strip to remove newline
        flag = 1
        break  # Exit loop once password is found

# If no password was found
if flag == 0:
    print("Password not found.")