def vigenere(plaintext, key):
	plaintext = plaintext.replace(" ","").lower()
	ciphertext = []
	key_pos = 0
	for c in plaintext:
		enc_char_val = (ord(c)-97 + ord(key[key_pos]) - 97) % 26
		enc_char = chr(enc_char_val+97)
		ciphertext.append(enc_char)

		key_pos += 1
		key_pos = key_pos % len(key)

	return "".join(ciphertext)


print vigenere("Why is a raven like a writing desk", "rabbithole")