print """
 __    __              _   ___                _     
/ / /\ \ \___  _ __ __| | / __\___  _ __ ___ | |__  
\ \/  \/ / _ \| '__/ _` |/ /  / _ \| '_ ` _ \| '_ \ 
 \  /\  / (_) | | | (_| / /__| (_) | | | | | | |_) |
  \/  \/ \___/|_|  \__,_\____/\___/|_| |_| |_|_.__/ 
       WordComb script by Guestik v0.1                                             
"""
listOfWords = list();
listOfResults = list();
nameOfFile = raw_input("Name of new file: ");
append = False;
import os
if os.path.isfile(nameOfFile + ".txt"):
  append = True;
  import imp
  try:
    imp.find_module('termcolor')
    imp.find_module('termcolor')
    from termcolor import colored
    print colored("Warning: File already exists! Going to append new words" , 'red');
  except ImportError:
    print "Warning: File already exists! Going to append new words";

#If file exists, add new words to it
#If file doesnt exist, create a new one
adding = True;
print "Let's add some words (to cancel adding enter q)";
while adding:
  addWord = raw_input("Add word: ");
  if addWord == "q":
    adding = False;
  else:
    if addWord: #If string is not empty
      listOfWords.append(addWord);

for x in range(0, len(listOfWords)):
  listOfResults.append(listOfWords[x]);
  for y in range(0, len(listOfWords)):
    listOfResults.append(listOfWords[x] + listOfWords[y]);
    for z in range(0, len(listOfWords)):
      listOfResults.append(listOfWords[x] + listOfWords[y] + listOfWords[z]);
      for w in range(0, len(listOfWords)):
        listOfResults.append(listOfWords[x] + listOfWords[y] + listOfWords[z] + listOfWords[w]);

xn = 0;
if append:
  f = open(nameOfFile + ".txt",'a')
else:
  f = open(nameOfFile + ".txt",'w')

for x in listOfResults:
  f.write(x + "\n")
  xn = xn+1;

f.close()
print str(xn) + " words created in " + nameOfFile + ".txt";
