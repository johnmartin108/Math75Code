p = "consistencyisthelastrefugeoftheunimaginative"
c = "voqimugocogmttfkxvlvdynhawugtfrsksoizgaanlygk"

for i in range(len(p)):
	if i % 3 == 0:
		print ""
	print "(" + str(ord(p[i]) - 97) +", " + str(ord(c[i]) - 97) + ")"

