"""Interactive Caesar cipher with punctuation preserved."""
def caesar(direction, text, shift):
    """Shift letters forward for encrypt or backward for decrypt."""
    if direction not in ('encrypt', 'decrypt'):
        raise ValueError('Direction must be encrypt or decrypt')
    delta = shift if direction == 'encrypt' else -shift
    output = []
    for char in text:
        if char.isascii() and char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            output.append(chr(base + (ord(char) - base + delta) % 26))
        else: output.append(char)
    return ''.join(output)
def encrypt(original_text, shift_amount):
    return caesar('encrypt', original_text, shift_amount)
def decrypt(original_text, shift_amount):
    return caesar('decrypt', original_text, shift_amount)
if __name__ == '__main__':
    while True:
        direction = input('encrypt or decrypt (or quit): ').strip().lower()
        if direction == 'quit': break
        if direction not in ('encrypt', 'decrypt'):
            print('Choose encrypt or decrypt.'); continue
        message = input('Text: ')
        try: shift = int(input('Shift: '))
        except ValueError:
            print('Shift must be a whole number.'); continue
        print(caesar(direction, message, shift))
