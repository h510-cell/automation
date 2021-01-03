import cv2
import time
import random
import dropbox

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() the method is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False
    return img_name
    print("snapShot taken")
    #release the camera
    videoCaptureObject.release()
    #closes all windows that might be opened while this process
    cv2.destroyAllWindows()

take_snapshot()

def upload_files(img_name):
    access_token = "sl.Aop_gOzjgI7jOKkadKAcvPt_MbkWOBCTNS2ee4v4shhMmvpWtaexWjdrIADb5sj7TX-kygUwW5F69mzitd_RtztVDyfcZ4PRdsRS3O7wzRKsuiyKKwjClSaLdvp9jaauZYaNE7E"
    file = img_counter
    file_from = file
    file_to = "/hemaagam/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")

def main():
    while(True):
        if ((time.time()- start_time) >= 300):
            name = take_snapshot()
            upload_files(name)

main()