#1A

#set up relevant constants
n = 2038667
ZZnZZ = Integers(n)
e = 103
m = 892383

ZZnZZ(m)^e #ANSWER

#1B

#compute q
n/1301

#find e^{-1} mod (p-1)(q-1), which works as a d
ZZpqZZ = Integers(1300*1566)
1/ZZpqZZ(103) #ANSWER

#1C
ZZnZZ(317730)^810367 #ANSWER