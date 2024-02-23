import os
import time

class LocystFileSort:
    initized = False
    imageExtensions = ['.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.png', '.gif', '.webp', '.tiff', '.tif', '.psd', '.raw', '.arw', '.cr2', '.nrw', '.k25', '.bmp', '.dib', '.heif', '.heic', '.ind', '.indd', '.indt', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.svg']
    videoExtensions = ['.webm', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg', '.mp4', '.mp4v', '.m4v', '.avi', '.wmv', '.mov', '.qt', '.flv', '.swf', '.avchd']
    audioExtensions = ['.m4a', '.flac', '.mp3', '.wav', '.wma', '.aac']
    documentExtensions = ['.doc', '.docx', '.odt', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx']

    documentFilePath = ''
    musicFilePath = ''
    videoFilePath = ''
    imageFilePath = ''

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

    @classmethod
    def sort(cls):
        if cls.initized is False:
            print("Run init before running other code")
            return 0
        
        for file in os.listdir(f'{cls.homeDir}/{cls.unsortedDir}'):
            cls.documentFilePath = f'{cls.homeDir}/Documents/{file}'
            cls.musicFilePath = f'{cls.homeDir}/Music/{file}'
            cls.videoFilePath = f'{cls.homeDir}/Videos/{file}'
            cls.imageFilePath = f'{cls.homeDir}/Pictures/{file}'
            cls.filePath = f'{cls.homeDir}/{cls.unsortedDir}/{file}'
            print(filePath)

            if os.path.isdir(filePath) is True:
                print(f"Folder detected: {file}")

            _, fileExtension = os.path.splitext(file)

            if fileExtension in cls.documentExtensions:
                os.replace(cls.filePath, cls.documentFilePath)
                print(f'Moved {file} to {cls.documentFilePath}')
            elif fileExtension in cls.musicExtensions:
                os.replace(cls.filePath, cls.musicFilePath)
                print(f'Moved {file} to {cls.musicFilePath}')
            elif fileExtension in cls.videoExtensions:
                os.replace(cls.filePath, cls.videoFilePath)
                print(f'Moved {file} to {cls.videoFilePath}')
            elif fileExtension in cls.imageExtensions:
                os.replace(cls.filePath, cls.imageFilePath)
                print(f'Moved {file} to {cls.imageFilePath}')
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
