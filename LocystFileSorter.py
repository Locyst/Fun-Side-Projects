import os
import time

class LocystFileSort:
    documentExtensions = ['.txt', '.md', '.pdf', '.doc']
    musicExtensions = ['.m4a', '.mp3', '.wav']
    videoExtensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
    imageExtensions = ['.png', '.jpg', '.jpeg']

    homeDir = './Files' # Put the directory that this program is going to be placed in
    unsortedDir = 'Unsorted' # Put either your downloads folder or another file that is going to have all of the unsorted files

    dirs = ['Documents', 'Pictures', 'Videos', 'Music',
      unsortedDir]
  
    @classmethod
    def init(cls):
        for directory in cls.dirs:
            path = os.path.join(cls.homeDir, directory)
            if not os.path.exists(path):
                os.makedirs(path)

    @classmethod
    def sort(cls):
        for file in os.listdir(f'{cls.homeDir}/{cls.unsortedDir}'):
            filePath = f'{cls.homeDir}/{cls.unsortedDir}/{file}'
            print(filePath)

            if os.path.isdir(filePath) is True:
                print(f"Folder detected: {file}")

            _, fileExtension = os.path.splitext(file)

            if fileExtension in cls.documentExtensions:
                os.replace(filePath, f'{cls.homeDir}/Documents/{file}')
            elif fileExtension in cls.musicExtensions:
                os.replace(filePath, f'{cls.homeDir}/Music/{file}')
            elif fileExtension in cls.videoExtensions:
                os.replace(filePath, f'{cls.homeDir}/Videos/{file}')
            elif fileExtension in cls.imageExtensions:
                os.replace(filePath, f'{cls.homeDir}/Pictures/{file}')
            else:
                print(f"Unknown file: {file}")
                print(fileExtension)


if __name__ == "__main__":
    print("Creating files")
    LocystFileSort.init()
    while (True):
        print("Sorting files")
        LocystFileSort.sort()
        time.sleep(300)
