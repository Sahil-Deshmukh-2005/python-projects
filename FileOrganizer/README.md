# File Organizer

***

Ever felt like your folder is getting messy and you need something to organize them, cause i did, and then i decided to make a `File Organizer`.  
Not Too much fancy but it does its job.  

***

## Features
I used already existing libraries in python.  
`os`,`shutil`, and `pathlib`   
I needed `os` to make the folder/directory and to remove a file, and `shutil` to move files from one folder to another, and `pathlib` ofcourse for the path itself.  

***

## Working
It sorts file on the basis of their suffix, i.e., `.txt`,`.pdf`,`.docx`, etc..  
It also returns the statistical data of our moved files.  
We are maintaining the `log` to see which file moves where.  

***

## How to run?
1) Run the file.  
2) Just enter the path where you want to perform the sorting.  
If you wanna sort in `pwd` or current directory just press `Enter`.  
❗But know that itll also sort `organizer.py` and `organizer.log` files which then will place `.log` file in `Others` directory, and wont get delet.
3) And `wallah` you have your sorted directory.  
4) Now if you wanna see which file moved where, just say `Y` to the next question, youll see the list of transfer happened, and `n` if you dont.
5) You can either keep the `log` file by saying `n` to next question or you can delete it just by pressing `Y`.

***

## Example
Example screenshots are in screenshots directory.

***
