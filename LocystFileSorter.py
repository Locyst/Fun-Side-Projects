"""
Automatically sorts files based on their type into folders
"""

import os
homeDir = './Files'
unsortedDir = './Unsorted'

def createFiles():
    dirs = [f'{homeDir}/Pictures', f'{homeDir}/Documents', f'{homeDir}/Music', f'{homeDir}/Videos', f'{homeDir}/{unsortedDir}']
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            pass

def sortFiles():
    documents = ['txt']
    music = ['m4a']
    videos = ['mp4']
    images = ['png', 'jpg', 'jpeg']
    if len(os.listdir(f'{homeDir}/{unsortedDir}')) > 0:
        for file in os.listdir(f'{homeDir}/{unsortedDir}'):
            if file.split('.')[1] in documents:
                os.replace(f'{homeDir}/{unsortedDir}/{file}', f'{homeDir}/Documents/{file}')
            elif file.split('.')[1] in music:
                os.replace(f'{homeDir}/{unsortedDir}/{file}', f'{homeDir}/Music/{file}')
            elif file.split('.')[1] in videos:
                os.replace(f'{homeDir}/{unsortedDir}/{file}', f'{homeDir}/Videos/{file}')
            elif file.split('.')[1] in images:
                os.replace(f'{homeDir}/{unsortedDir}/{file}', f'{homeDir}/Pictures/{file}')
            else:
                print(f"Unknown file: {file}")
                pass
    else:
        print("No files to sort")

if __name__ == "__main__":
    print("Creating files")
    createFiles()
    print("Sorting files")
    sortFiles()
