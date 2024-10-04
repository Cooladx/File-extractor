import glob, os, pathlib
from pathlib import Path
import sys




def extractFiles():
    print("Welcome to the file extractor")
   
    message = ""
    while message != "yes":
        fileholder = []
        try:
            sourceFolder = input("Please input the folder you wish to extract from: ")
            print("\nHere's what in your directory.\n")
            # Looks for absolute path if user does from root directory. 
            if os.path.isabs(sourceFolder):
                extractPath = sourceFolder
            
            # Will do relative path instead
            else:
                extractPath = str(Path.home() / sourceFolder)

           # display files regardless of relative or absolute path
            print(os.listdir(extractPath))
        
        except FileNotFoundError:
            print("\nDouble check your file path to ensure it's correct.\n")
            sys.exit()

        extractFileExtension = input("\n\n Which file extension would you like to extract: ")

        os.chdir(extractPath)
        # Appended dot so user doesn't have to type that in. 
        for file in glob.glob("*." + extractFileExtension):
            # appends each file and add it to the list
            fileholder.append(file)
        print("\n\n")
        print(fileholder)
        print("\nWhere do you want these files to go?")
          
        # Takes user input to move destinated files to a given location in their file system
        destinationPath = input()


        # Iterate through all files in the list of fileholder which you will be transfering.
        for file in fileholder:
            # Takes full path of one file to return itself as a file and destination path is where file will be sent.
            destFile = os.path.join(destinationPath, os.path.basename(file))
            os.rename(file, destFile)
            print(file + " has been moved to " + destinationPath)


        print("\n\nAre you finished with the program? type 'yes' to exit")
        # Allows user to quit with yes. Otherwise, run the program again.
        message = input()



# Starting main code
extractFiles()
