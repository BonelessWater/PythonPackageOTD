'''
Day 12, June 17th 2025: 

Welcome to steganography!

Hide secret messages inside innocent-looking images.
Perfect for covert communication or just impressing friends.
The image looks normal, but contains hidden data that only
you know how to extract. Digital invisibility at its finest.
'''

from PIL import Image
import numpy as np

def hide_message(img_path, msg, out_path):
    img = np.array(Image.open(img_path))
    binary = ''.join(format(ord(c), '08b') for c in msg) + '1111111111111110'
    flat = img.flatten()
    for i, bit in enumerate(binary[:len(flat)]):
        flat[i] = (flat[i] & 0xFE) | int(bit)
    Image.fromarray(flat.reshape(img.shape).astype('uint8')).save(out_path)

def extract_message(img_path):
    flat = np.array(Image.open(img_path)).flatten()
    bits = [str(p & 1) for p in flat]
    msg = ""
    for i in range(0, len(bits), 8):
        byte = ''.join(bits[i:i+8])
        if byte == '11111110': break
        msg += chr(int(byte, 2))
    return msg

# Demo: Hide and extract a secret message
secret = "This is not the real secret message."
hide_message('youre_cooked.png', secret, 'AmI.png')
revealed = extract_message('AmI.png')
print(f"✅ Message hidden in AmI.png")
print(f"🔍 Extracted: {revealed}")