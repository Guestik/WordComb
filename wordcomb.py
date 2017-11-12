print "WordComb Script by Guestík";
listOfWords = list();
nameOfFile = raw_input("Name of new file: ");
#If file exists, already existing words in file add to list and then add new words
#If file doesnt exists, create a new one
addWord = raw_input("Add word: ");
listOfWords.append(addWord);
print "Bye";
