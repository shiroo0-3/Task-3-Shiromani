import string
import secrets
import math
# Get password length from user
while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")
# Create character pool
characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)
# Generate password
password = ''.join(
    secrets.choice(characters)
    for _ in range(length)
)
# Calculate entropy
entropy = length * math.log2(len(characters))
# Display results
print("\nGenerated Password:")
print(password)
print("\nPassword Details")
print("----------------")
print("Length:", length)
print("Character Pool Size:", len(characters))
print("Entropy: {:.2f} bits".format(entropy))
if entropy >= 80:
    print("Security Level: Very Strong")
elif entropy >= 60:
    print("Security Level: Strong")
else:
    print("Security Level: Moderate")