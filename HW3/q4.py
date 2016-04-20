ciphertext = "mgodt beida psgls akowu hxukc iawlr csoyh prtrt udrqh cengx" \
+"uuqtu habxw dgkie ktsnp sekld zlvnh wefss glzrn peaoy lbyig"\
+"uaafv eqgjo ewabz saawl rzjpv feyky gylwu btlyd kroec bpfvt"\
+"psgki puxfb uxfuq cvymy okagl sactt uwlrx psgiy ytpsf rjfuw"\
+"igxhr oyazd rakce dxeyr pdobr buehr uwcue ekfic zehrq ijezr"\
+"xsyor tcylf egcy"

ciphertext = ciphertext.replace(" ", "")

for i in range(1, 15):
	coincidences = 0
	for j in range(len(ciphertext)-i):
		if ciphertext[j] == ciphertext[j+i]:
			coincidences += 1

	print i, coincidences


trigrams = {}
for i in range(len(ciphertext)-3):
	if ciphertext[i:i+3] not in trigrams:
		trigrams[ciphertext[i:i+3]] = [i]
	else:
		trigrams[ciphertext[i:i+3]].append(i)

for key in trigrams:
	if len(trigrams[key]) > 1:
		print key, trigrams[key]