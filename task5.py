from Crypto.Util import *
from Crypto.Cipher import *
from padding import pad, unpad
from base64 import b64encode
import sys

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