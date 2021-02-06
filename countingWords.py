introstring = input("Enter any string : ")
charcounter = 0
wordcount=1
for i in introstring:
    charcounter=charcounter+1
    if(i==" "):
        wordcount=wordcount+1
print("Number of words in the string : ")
print(wordcount)
print("Number of characters in the string : ")
print(charcounter)