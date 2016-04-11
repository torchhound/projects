def bowlingScore(score):
	totalScore = 0
	scorePtr = 0
	for x in string:
		if x is 'X' or 'x':
			totalScore + 10 + score[scorePtr + 1] + score[scorePtr  + 2]
		elif x is '/':
			totalScore + 10 + score[scorePtr  + 1]
		else:
			totalScore + x
		scorePtr += 1
	print(totalScore)
	
def main():
	userScore = input("Please input a bowling score without spaces: ")
	bowlingScore(userScore)
	
main()