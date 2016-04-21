'''
    The "fog index" of a passage of text estimates its reading difficulty, as a number corresponding roughly to a school grade level. For example, a passage with a fog index of 12 should be comprehensible to anyone with 12 years of schooling.

    The Gunning version of the fog index uses the following algorithm.

        Choose a section of the text at least 100 words in length.

        Count the number of sentences (a portion of a sentence truncated by the boundary of the text section counts as one).

        Find the average number of words per sentence.

        AVE_WDS_SEN = TOTAL_WORDS / SENTENCES

        Count the number of "difficult" words in the segment -- those containing at least 3 syllables. Divide this quantity by total words to get the proportion of difficult words.

        PRO_DIFF_WORDS = LONG_WORDS / TOTAL_WORDS

        The Gunning fog index is the sum of the above two quantities, multiplied by 0.4, then rounded to the nearest integer.

        G_FOG_INDEX = int ( 0.4 * ( AVE_WDS_SEN + PRO_DIFF_WORDS ) )

    Step 4 is by far the most difficult portion of the exercise. There exist various algorithms for estimating the syllable count of a word. A rule-of-thumb formula might consider the number of letters in a word and the vowel-consonant mix.

    A strict interpretation of the Gunning fog index does not count compound words and proper nouns as "difficult" words, but this would enormously complicate the script.
	'''

import re

def fileOpen(filename):
	obj = open(filename, "r")
	ret = obj.readlines()
	return ret
	
def findSentences(text):


def longWords(text):

	
def fogIndex(text): 
	size = len(text)
	if size >= 100:
		sentNum = findSentences(text)
		avrWords = size / sentNum
		longWords = longWords(text)
		diffWords = longWords / size
		indexTotal = (0.4 * (avrWords + diffWords))
		return int(indexTotal)
	else:
		return False
		
def main():
	userInput = input("Enter a text file for Fog Index calculation: ")
	fogIndex(fileOpen(userInput))
	
if __name__ == '__main__':
	main()
