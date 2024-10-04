# File-extractor

Getting tired of going through files and picking out each one to send to another location?

The purpose of this python program is to take user input from their home or root directory. You may do a relative path 
from the home directory which could look like something like this:

Downloads, General, test, Templates, pictures, Music, Videos, etc. You'd only put those single paths because they are a location that is relative to a current directory which is your home directory in this case.

DO NOT DO /Documents for example. Just enter Documents. Think of relative paths as the position you are currently on and you're moving to xyz position that is right next to you instead of going to the beginning.



On the subject of ABSOLUTE PATHS:

 you'll get an absolute path which starts from root that is /

If you were to take files, it would be something like /home/user/General/codeProjects. Remember, absoulte path will start with / because that is the root of your filesystem. I'd like to think of it as a start to finish for a running marathon on a determined path you are supposed to take. Always start with / when transfering all files to another directory.


See the difference? 

Running the program itself:

1. The program itself extracts source path which could be relative path or absolute path (your choice depending on how far away your files are from home directory). 

2. Then, it displays what's in the directory. Afterwards, it gives the user another input for what file extension they would like to enter.

3. All files would be shown just to verify if you are sure you want to move all these files of a specific extension.

4. Lastly, you would again specify an absolute path for where the file extracted would go which is your destination path. Don't do relative path if you were to do Documents for example. Instead, do /home/user/Documents and that will work.

5. Program is intended to run until user types "yes". 


This program is meant to be for linux, just something I'd like to implement because I'm lazy lol.

Now you can be happy your downloads folder is not clogged with nonsense! 


