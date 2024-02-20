import os
import time

class LocystFileSort:
    initized = False
    documentExtensions = ['.txt', '.md', '.pdf', '.doc']
    musicExtensions = ['.m4a', '.mp3', '.wav']
    videoExtensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
    imageExtensions = ['.png', '.jpg', '.jpeg']

    homeDir = './Files' # Put the directory that this program is going to be placed in
    unsortedDir = 'Unsorted' # Put either your downloads folder or another file that is going to have all of the unsorted files
    filePath = ''

    dirs = ['Documents', 'Pictures', 'Videos', 'Music',
      unsortedDir]
  
    @classmethod
    def init(cls):
        cls.initized = True
        for directory in cls.dirs:
            path = os.path.join(cls.homeDir, directory)
            if not os.path.exists(path):
                os.makedirs(path)
        cls.filePath = f'{cls.homeDir}/{cls.unsortedDir}/{file}'

    @classmethod
    def sort(cls):
        if cls.initized is False:
            print("Run init before running other code")
            return 0
        
        for file in os.listdir(f'{cls.homeDir}/{cls.unsortedDir}'):
            print(filePath)

            if os.path.isdir(filePath) is True:
                print(f"Folder detected: {file}")

            _, fileExtension = os.path.splitext(file)

            if fileExtension in cls.documentExtensions:
                os.replace(cls.filePath, f'{cls.homeDir}/Documents/{file}')
            elif fileExtension in cls.musicExtensions:
                os.replace(cls.filePath, f'{cls.homeDir}/Music/{file}')
            elif fileExtension in cls.videoExtensions:
                os.replace(cls.filePath, f'{cls.homeDir}/Videos/{file}')
            elif fileExtension in cls.imageExtensions:
                os.replace(cls.filePath, f'{cls.homeDir}/Pictures/{file}')
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
