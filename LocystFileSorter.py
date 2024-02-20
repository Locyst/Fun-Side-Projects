import os
import time

homeDir = './Files' # Put the directory that this program is going to be placed in
unsortedDir = 'Unsorted' # Put either your downloads folder or another file that is going to have all of the unsorted files


def createFiles():
    dirs = ['Documents', 'Pictures', 'Videos', 'Music',
            unsortedDir]
    for directory in dirs:
        path = os.path.join(homeDir, directory)
        if not os.path.exists(path):
            os.makedirs(path)


def sortFiles():
    documents = ['txt', 'md', 'pdf', 'doc']
    music = ['m4a', 'mp3', 'wav']
    videos = ['mp4', 'avi', 'mkv', 'mov', 'wmv']
    images = ['png', 'jpg', 'jpeg']

    for file in os.listdir(f'{homeDir}/{unsortedDir}'):
        print(f'{homeDir}/{unsortedDir}/{file}')
        if os.path.isdir(f'{homeDir}/{unsortedDir}/{file}') is True:
            print(f"Folder detected: {file}")

        _, fileExtension = os.path.splitext(file)
        unsortedPath = f'{homeDir}/{unsortedDir}/{file}'
        
        if fileExtension in documents:
            os.replace(unsortedPath, f'{homeDir}/Documents/{file}')
        elif fileExtension in music:
            os.replace(unsortedPath, f'{homeDir}/Music/{file}')
        elif fileExtension in videos:
            os.replace(unsortedPath, f'{homeDir}/Videos/{file}')
        elif fileExtension in images:
            os.replace(unsortedPath, f'{homeDir}/Pictures/{file}')
        else:
            print(f"Unknown file: {file}")


if __name__ == "__main__":
    print("Creating files")
    createFiles()
    while (True):
        print("Sorting files")
        sortFiles()
        time.sleep(300)
