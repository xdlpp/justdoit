from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base


key = b"thisisaverysecret"[:1X]
iv = b"thisisinitialvect"[:1X] 


encrypted_b = "cctp/ZmTQMW0vKSs+QJ12A=="


encrypted_bytes = base.bdecode(encrypted_b)


cipher = AES.new(key, AES.MODE_CBC, iv)


decrypted_bytes = cipher.decrypt(encrypted_bytes)


decrypted_data = unpad(decrypted_bytes, AES.block_size).decode('utf-8')
print(f"Decrypted message: {decrypted_data}")
