# Compress folders and files
import zipfile as zf
import os

# compress files
def compress_files(files):
    with zf.ZipFile("compress", 'w') as myzip:
        for file in files:
            myzip.write(file)
            
# compress folders
def compress_folders(folders):
    with zf.ZipFile("compress", 'w') as myzip:
        for folder in folders:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    myzip.write(os.path.join(root, file))
                    
# main 
compress_files(["video1.mp4", "video2.mp4"])
compress_folders(["folder1", "folder2"])
