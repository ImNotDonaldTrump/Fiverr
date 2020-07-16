
#function section

try:
    def fileScraping():                                                                                                 # defining the file word, character "searching"
        numberParagraph = -1                                                                                            # var for number of the Paragraphs
        numberLines  = 0                                                                                                # var for number of the Lines
        numberWords = 0                                                                                                 # var for number of the Words
        numberWordsInFile = 0                                                                                           # var for number of the Words in the File
        numberChars = 0                                                                                                 # var for number of the Characters
        with open (file, "r") as objectFile:                                                                            # opening the file
            for line in objectFile:                                                                                     # for every line in the file the code will be executed
                words = line.split()                                                                                    # a line will be split in the wirds
                numberLines += 1                                                                                        # adding 1 for every line
                numberWords += len(words)                                                                               # adding the items of that object
                numberChars += len(line)                                                                                # adding the items of that object
                numberWordsInFile += len(words)                                                                         # adding the items of that object


                if line in ['\n', '\r\n']:                                                                              # if a line is blank the code under will be executed
                    numberParagraph += 1                                                                                # adding 1 to the numberParagraph
                    print("")                                                                                           # blank space
                    print("Paragraph " + str(numberParagraph))                                                          # printing out the paragraph, etc
                    print("  Number of lines in the paragraph : " + str(numberLines))
                    print("  Number of words in the paragraph : " + str(numberWords))
                    print("  Number of characters in the paragraph : " + str(numberChars))
                    fileCreate = open(fileCreateName + ".out", "w+")                                                    # opening/creating the wanted file
                    fileCreate.write("Paragraph " + str(numberParagraph) + "\n")                                        # writing the paragraph, etc in the wanted file
                    fileCreate.write("  Number of liness in the paragraph : " + str(numberLines) + "\n")
                    fileCreate.write("  Number of words in the paragraph : " + str(numberWords) + "\n")
                    fileCreate.write("  Number of characters in the paragraph : " + str(numberChars) + "\n")

                    numberLines = 0                                                                                     # resetting the variables
                    numberWords = 0
                    numberChars = 0

        print("")
        numberParagraph += 1                                                                                            # adding 1 to the numberParagraph
        print("Paragraph " + str(numberParagraph))                                                                      # printing the number of paragraph etc out
        print("  Number of lines in the paragraph : " + str(numberLines))
        print("  Number of words in the paragraph : " + str(numberWords))
        print("  Number of characters in the paragraph : " + str(numberChars))
        print("")
        print("  Number of words in the file : " + str(numberWordsInFile))

        fwileCreate = open(fileCreateName + ".out", "w+")                                                               # opening the wanted file again
        fileCreate.write("Paragraph " + str(numberParagraph) + "\n")                                                    # printing in the file
        fileCreate.write("  Number of lines in the paragraph : " + str(numberLines) + "\n")
        fileCreate.write("  Number of words in the paragraph : " + str(numberWords) + "\n")
        fileCreate.write("  Number of characters in the paragraph : " + str(numberChars) + "\n")
        fileCreate.write("----------------------------------------------\n")
        fileCreate.write("Number of words in the file :" + str(numberWordsInFile))
        fileCreate.write("----------------------------------------------\n")

except:
    print("File Error")

#input section
fileName = input("Name of the input file (x.in/txt) : ")                                                                # input for the name/path to the input file
fileCreateName = input("Name of the .out file :")                                                                       # input for the name of the created file

file = fileName

#execution Section

fileScraping()                                                                                                          # executing the defined code
