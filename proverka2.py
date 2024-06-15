import os
SECRET_KEY = os.urandom(24).hex()
print(SECRET_KEY)