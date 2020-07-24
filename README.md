# Python
Projects with Python
Hi friends!
This project is about some solutions I developed
## WEB Downloader
The folder "WEB_Downloader" is a program that log into a JSP Web site and be free to download files.
After that, the program read a list of URL from a Excel file and do download one by one to a temporary folder (triangulation starts)
After download the file is named with a server format name, but needs to be renamed to other name. Than the file is renamed and moved to destin folder (triangulations ended).
to enter into web I used the library Selenium that controls a webdriver (I choose Chrome navigator) and not permit to control download stages.
To control the download phases (start, progress, finish) I used the OS Library and file system.
I used a triangulation with a temp folder to control the name of file, because I needed to rename the file after finish, but I did not know the name of file before finish.
After finish download I renamed the file and moved It to destination folder.
To control the flow I read all files downloaded and not perform same download, if the file has 2 same names, the second file does not be downloaded (make sense!)
The list has about 1000 files, it make sense to control the flow of downloads and permit resume other day.
This project was sucessful executed, and has gain of 60% of production time. It was did manually and much time expended.
