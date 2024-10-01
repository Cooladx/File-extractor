import os
from pathlib import Path


# Need OS module to interact with the file system
# need Path module to get the path of the Downloads folder and possibly move file extensions to whatever user wishes to specify.
# Set download_path to 
# Will check Downloads folder
# Get the following file extensions from downloads
# If file is a .pdf
    # Extract that pdf file, send it to a folder documents (You can also change this, but for now default as documents), and send to folder (which ever destination you wish)

# Else if 

folder = input("Please input the folder you wish to extract from: ")


extractPath = str(Path.home() / folder)

print("Here's what in your directory.")
print(os.listdir(extractPath))
extractFile = input("Which file extension would you like to enter:")


   