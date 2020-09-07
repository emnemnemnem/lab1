from Crypto.Util import *
from Crypto.Cipher import *
from padding import pad, unpad
from base64 import b64encode

hex_iv = 'aabbccddeeff00998877665544332211'
iv_bytes = bytes.fromhex(hex_iv)

plaintext = b"you captured the flag"
padded = pad(plaintext,16)

key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_CBC, iv_bytes)