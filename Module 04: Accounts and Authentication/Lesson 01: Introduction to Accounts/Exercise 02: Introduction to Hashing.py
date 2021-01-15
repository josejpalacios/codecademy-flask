# Important rule of application development is to never store sensitive user data as plain text.

# Hashing: Process of taking text input and creating a new sequence of characters out of it that cannot be easily reverse-engineered.

# Add hashing functionality to a Flask application using the security module of the Werkzeug package.

# generate_password_hash(): Takes a string as an argument and returns a hash of the string
# check_password_hash(): Takes two arguments, the hashed string and a new string which we are checking the hash against.
#                        It returns a boolean indicating if the string was a match to the hash.

# import generate_password_hash and check_password_hash here:
from werkzeug.security import generate_password_hash, check_password_hash


hardcoded_password_string = "123456789_bad_password"

# generate a hash of hardcoded_password_string here:
hashed_password = generate_password_hash(hardcoded_password_string)
# print hashed_password
print(hashed_password)

password_attempt_one = "abcdefghij_123456789"

# check password_attempt_one against hashed_password here:
hash_match_one = check_password_hash(hashed_password, password_attempt_one)
# print hash_match_one
print(hash_match_one)

password_attempt_two = "123456789_bad_password"

# check password_attempt_two against hashed_password here:
hash_match_two = check_password_hash(hashed_password, password_attempt_two)
# print hashed_match_two
print(hash_match_two)
