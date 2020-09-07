from Crypto.Util import *
from Crypto.Cipher import *
from padding import pad, unpad
from base64 import b64encode
import sys

hex_iv = 'aabbccddeeff00998877665544332211'
iv = int(hex_iv,16)

bytes_ptxt1 = b"you captured the"
hex_ptxt1=bytes_ptxt1.hex()
ptxt1=int(hex_ptxt1,16)

bytes_ptxt2 = b" flag"
bytes_ptxt2_padded=pad(bytes_ptxt2,16)
hex_ptxt2=bytes_ptxt2_padded.hex()
ptxt2=int(hex_ptxt2,16)

hex_cipher1='46beb3b832973495f79b860884245e43'
hex_cipher2='1d73c2d3f7e3a7632dce894ed14ff62b'
cipher1=int(hex_cipher1,16)
cipher2=int(hex_cipher2,16)

# xor of IV and first 16 bytes of plaintext -- outputs with int
xor = iv^ptxt1
print("xor: ", xor)
# xor2 is xor of last 16 bytes of plaintext and first 16 of ciphertext
xor2 = cipher1^ptxt2
print("xor2: ", xor2)