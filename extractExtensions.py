import glob, os, pathlib
from pathlib import Path
import sys





# Keep in the local scope so it doesn't keep getting initized. 
storageExtension = []

message = print("Hello, welcome to the file extractor")



# Program will keep running until user enters yes, meaning they want to exit.
while (message != "yes"): 

    
    try:
        folder = input("Please input the folder you wish to extract from: ")
        print("\n\nHere's what in your directory.\n\n")
        extractPath = str(Path.home() / folder)
        print(os.listdir(extractPath))
         


    except FileNotFoundError:
            print("\nDouble check your file path to ensure it's correct.\n")        
            sys.exit()
       
   
  
    extractFileExtension = input("\n\n Which file extension would you like to extract: ")

    
    if extractFileExtension not in storageExtension:
         storageExtension.append(extractFileExtension)
         os.chdir(extractPath)
    for file in glob.glob("*." + extractFileExtension):
         print(file)
    
        
  
   




      # User input to terminate with yes if they want to.
    print("Are you finished with the program? type 'yes' to exit")
    message = input()
   