import os
import shutil
import time

home_dir = os.path.expanduser("~")
main_dir = os.path.join(home_dir, "Downloads", "Sorter")
downloads_dir = os.path.join(home_dir, "Downloads")

folders = ["Archive Files", "Image Files", "Executable Files", "Document Files", "Video Files", "Audio Files",
           "Other Files"]
docs = ["Word Documents", "Excel Documents", "Powerpoint Presentations", "PDF", "Text Files"]
docs_dir = os.path.join(main_dir, "Document Files")

ar_ext = [".rar", ".7z", ".zip", ".tar", ".tar.gz"]

img_ext = [".apng", ".avif", ".gif", "jfif", ".pjpeg", "pjp", "svg", "webp", ".png", ".jpeg", ".jpg", ".ico", ".bmp"]
vid_ext = [".mp4", ".mov", ".wmv", ".avi", ".m4v", ".mkv", ".mpg", ".mpeg", ".mp2", ".mpv", ".m4p", ".m4v", ".flv"]
audio_ext = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac", ".ogg"]
# INSIDE DOCUMENT FILES
word_ext = [".docx", ".doc", ".docm", ".dot", ".dotm", ".dotx", ".docb"]
xl_ext = [".xlsx", ".xlsm", ".xlsb", ".xltx", ".xltm", ".xls", ".xlt", ".xls"]
ppt_ext = [".pptx", ".pptm", ".ppt"]

non_ext = [".ini", ".opdownload", ".crdownload"]

ar_ext = ar_ext + list(map(lambda x: x.upper(), ar_ext))
img_ext = img_ext + list(map(lambda x: x.upper(), img_ext))
vid_ext = vid_ext + list(map(lambda x: x.upper(), vid_ext))
audio_ext = audio_ext + list(map(lambda x: x.upper(), audio_ext))
xl_ext = xl_ext + list(map(lambda x: x.upper(), xl_ext))
ppt_ext = ppt_ext + list(map(lambda x: x.upper(), ppt_ext))
word_ext = word_ext + list(map(lambda x: x.upper(), word_ext))


def file_creation():
    os.mkdir(main_dir)
    for f in folders:
        os.mkdir(os.path.join(main_dir, f))
    for d in docs:
        os.mkdir(os.path.join(docs_dir, d))


def check_file():
    if os.path.isdir(main_dir):
        for f in folders:
            if not os.path.isdir(os.path.join(main_dir, f)):
                os.mkdir(os.path.join(main_dir, f))
        for d in docs:
            if not os.path.isdir(os.path.join(docs_dir, d)):
                os.mkdir(os.path.join(docs_dir, d))
    else:
        file_creation()


def ext_sort2():
    # Check if it's a folder
    # if it is a folder, ignore it
    # then iterate all files and check
    for d in os.listdir(downloads_dir):
        file = os.path.splitext(d)
        if not os.path.isdir(os.path.join(downloads_dir, d)):
            if file[1] in ar_ext:
                shutil.move(os.path.join(downloads_dir, d), os.path.join(main_dir, folders[0], d))
            elif file[1] in img_ext:
                shutil.move(os.path.join(downloads_dir, d), os.path.join(main_dir, folders[1], d))
            elif file[1] == ".exe" or file[1] == ".EXE":
                shutil.move(os.path.join(downloads_dir, d), os.path.join(main_dir, folders[2], d))
            elif file[1] in word_ext:
                shutil.move(os.path.join(downloads_dir, d), os.path.join(main_dir, folders[3], docs[0], d))
            elif file[1] in xl_ext:
                shutil.move(os.path.join(downloads_dir, d), os.path.join(main_dir, folders[3], docs[1], d))
            elif file[1] in ppt_ext:
                shutil.move(os.path.join(downloads_dir, d), os.path.join(main_dir, folders[3], docs[2], d))
            elif file[1] == ".pdf" or file[1] == ".PDF":
                shutil.move(os.path.join(downloads_dir, d), os.path.join(main_dir, folders[3], docs[3], d))
            elif file[1] == ".txt" or file[1] == ".TXT":
                shutil.move(os.path.join(downloads_dir, d), os.path.join(main_dir, folders[3], docs[4], d))
            elif file[1] in vid_ext:
                shutil.move(os.path.join(downloads_dir, d), os.path.join(main_dir, folders[4], d))
            elif file[1] in audio_ext:
                shutil.move(os.path.join(downloads_dir, d), os.path.join(main_dir, folders[5], d))


if __name__ == '__main__':
    print("Running the sorter!")
    check_file()
    while 1:
        ext_sort2()
        time.sleep(0.5)
