def konami(userInput):
	konamiCode = "uuddlrabs"
	count = 0
	lst = []
	for x in userInput:
		lst.append(x)
		#count += 1
		#if count % 9 == 0:
		code = ""
		for x in lst:
			code += x
		if code in konamiCode:
			return True
		else:
			pass
		#if count % 9 == 0:
	#		lst = []
			#pass
	return False

print(konami("dasfjajfdfjhsdjkfjhksdfuuddlrabs"))
print(konami("uuddlrabsaskjfjhasfhjfllfasfllsa"))
print(konami("asjdaljsfljuuddlrabssadasfasffsf"))
