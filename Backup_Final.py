import datetime
import shutil
import os
import zipfile

# Todays date and time
todays_date = datetime.datetime.now()
format_date = todays_date.strftime("_%d_%m_%Y_%H%M%S")

# New directory named Backup + today's date
new_directory = "Backup" + format_date

# Copy the content of Data into the new backup folder
source = 'C:\\files\\data'
destination = 'C:\\files\\backup\\' + new_directory
copy_to_dst = shutil.copytree(source, destination)
print("Backup completed. Your files are stored here: " + destination)

# Zip the newly created backup folder
os.chdir('C:\\files\\backup')
zip_dir = new_directory

with zipfile.ZipFile(new_directory + ".zip", 'w', zipfile.ZIP_DEFLATED) as newzip:
    for dirpath, dirnames, files in os.walk(zip_dir):
        for file in files:
            newzip.write(os.path.join(dirpath, file))

# Deletes the original backup folder
os.chdir('C:\\files\\backup')
delete_folder = "Backup_07_03_2022_214506"
try:
    shutil.rmtree(delete_folder)
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

# User can select Yes or No to open main backup folder
open_backup_dir: str
open_backup_dir = input("Do you want to open the main backup folder Y/N: ")
while open_backup_dir.upper() != "Y" and open_backup_dir.upper() != "N":
    print(" ")
    print("Type N or Y")
    open_backup_dir = input("Do you want to open the main backup folder Y/N: ")

if open_backup_dir.upper() == "Y":
    os.startfile('C:\\files\\backup')
    print("Backup script finished")
else:
    print("Backup script finished")