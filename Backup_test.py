# backup guide
# https://www.geeksforgeeks.org/automate-backup-with-python-script/

# How to open a directory / folder
# https://www.codegrepper.com/code-examples/python/how+to+open+folder+in+python

# Copy tree - Copy content of a folder
# https://www.geeksforgeeks.org/python-shutil-copytree-method/

# How to zip a file
# https://www.youtube.com/watch?v=Tg0kSsxW7ro

# How to open a foldder
# https://www.youtube.com/watch?v=wmJba8XicU0&t=50s

import datetime  # date and time
import shutil  # copy of files
import os  # status on files, go to a path
import zipfile  # zip and compress a file

# Today's date and time
todays_date = datetime.datetime.now()
format_date = todays_date.strftime("_%d_%m_%Y_%H%M%S")

# New directory named Backup + today's date
new_directory = "Backup" + format_date

# Copy the content of Data into the new backup folder
source = 'C:\\files\\data'
destination = 'C:\\files\\backup\\' + new_directory
copy_to_dst = shutil.copytree(source, destination)
print("")
print("Backup completed. Your files are stored here: " + destination)

# Zip the newly created backup folder
os.chdir('C:\\files\\backup')
zip_dir = new_directory

with zipfile.ZipFile(zip_dir + ".zip", 'w', zipfile.ZIP_DEFLATED) as newzip:
    for dirpath, dirnames, files in os.walk(zip_dir):
        for file in files:
            newzip.write(os.path.join(dirpath, file))

# Deletes the original backup folder
# os.chdir('C:\\files\\backup') We are already in this path, otherwise you will need to write this.
delete_folder = new_directory
shutil.rmtree(delete_folder)

# User can select Yes or No to open main backup folder
open_backup_dir: str
open_backup_dir = input("Do you want to open the main backup folder Y/N: ")
while open_backup_dir.upper() != "Y" and open_backup_dir.upper() != "N":
    print("")
    print("Type N or Y")
    open_backup_dir = input("Do you want to open the main backup folder Y/N: ")

class backup_done:
    def messasge():
        print("Backup script finished")

if open_backup_dir.upper() == "Y":
    os.startfile('C:\\files\\backup')
    backup_done.messasge()
else:
    backup_done.messasge()

# unzip files
# folder_to_be_zipped = 'news_unzipped'
# with zipfile.ZipFile('testzip.zip', 'r') as zip_ref:
#     zip_ref.extractall(folder_to_be_zipped)

