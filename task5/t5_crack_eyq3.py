from Crypto.Util import *
from Crypto.Cipher import *
from padding import pad, unpad
from base64 import b64encode
import sys
import os

# Below is copyright notice for padding functions
#
# Util/Padding.py :  Functions to manage padding
#
# ===================================================================
#
# Copyright (c) 2014, Legrandin <helderijs@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ===================================================================

hex_iv = 'aabbccddeeff00998877665544332211'
iv = int(hex_iv,16)
# convert hex to 16-byte iv
bytes_iv = bytes.fromhex(hex_iv)

with open(os.path.join(sys.path[0], "plaintext"), "r") as f:
    plaintext = f.read().encode('utf-8')
padded = pad(plaintext, 16)

hex_cipher='46beb3b832973495f79b860884245e431d73c2d3f7e3a7632dce894ed14ff62b'
bytes_cipher = bytes.fromhex(hex_cipher)

with open(os.path.join(sys.path[0], "words.txt"), "r") as key_file:
  for line in key_file:
    potential_key = line.strip()
    if (len(potential_key) > 16):
        continue
    if (len(potential_key) < 16):
        hash_number = 16-len(potential_key)
        hashes = "#"*hash_number
        potential_key+=hashes
    bytes_pkey = potential_key.encode('utf-8')
    cipher = AES.new(bytes_pkey, AES.MODE_CBC, bytes_iv)
    compare_cipher = cipher.encrypt(padded)
    if (bytes_cipher == compare_cipher):
        key = potential_key
        print(key)
        break