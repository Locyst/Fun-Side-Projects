import os
import time

homeDir = './Files'
unsortedDir = 'Unsorted'

def createFiles():
    dirs = [f'{homeDir}/Pictures', f'{homeDir}/Documents', f'{homeDir}/Music', f'{homeDir}/Videos', f'{homeDir}/{unsortedDir}']
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            pass

def sortFiles():
    documents = ['txt', 'md', 'pdf', 'doc']
    music = ['m4a', 'mp3', 'wav']
    videos = ['mp4', 'avi', 'mkv', 'mov', 'wmv']
    images = ['png', 'jpg', 'jpeg']

    for file in os.listdir(f'{homeDir}/{unsortedDir}'):
        print(f'{homeDir}/{unsortedDir}/{file}')
        if os.path.isdir(f'{homeDir}/{unsortedDir}/{file}') is True:
            print(f"Folder detected: {file}")


        fileParts = file.split('.')
        if len(fileParts) > 1:
            fileExtension = fileParts[-1]
            if fileExtension in documents:
                os.replace(f'{homeDir}/{unsortedDir}/{file}', f'{homeDir}/Documents/{file}')
            elif fileExtension in music:
                os.replace(f'{homeDir}/{unsortedDir}/{file}', f'{homeDir}/Music/{file}')
            elif fileExtension in videos:
                os.replace(f'{homeDir}/{unsortedDir}/{file}', f'{homeDir}/Videos/{file}')
            elif fileExtension in images:
                os.replace(f'{homeDir}/{unsortedDir}/{file}', f'{homeDir}/Pictures/{file}')
            else:
                print(f"Unknown file: {file}")
        else:
            print(f"Missing file extension: {file}")

if __name__ == "__main__":
    print("Creating files")
    createFiles()
    while (True):
        print("Sorting files")
        sortFiles()
        time.sleep(300)
