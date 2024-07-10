sentence = input("Enter your sentence for converted reversed word: ")
words = sentence.split()  
reversedWords = words[::-1]  
reversedSentence = " ".join(reversedWords)  

print("Your sentence converted in reversed word" "\n", reversedSentence)  

