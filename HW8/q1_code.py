ZZnZZ = Integers(27781703927)

AtoB = ZZnZZ(5)**1002883876 #Alice chooses a, sends Bob g^a
BtoA = ZZnZZ(5)**21790753397 #Bob chooses b, sends Alice g^b
SK = ZZnZZ(AtoB)**21790753397 #secret key is g^ab, or (g^a)^b