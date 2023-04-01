import cv2  
import os  
from PIL import Image 
import glob 
 
 
def convert_video_into_images(video_path): 
    # Read the video from specified path  
    camera = cv2.VideoCapture(video_path)  
 
    # set current frame to zero  
    current_frame = 0 
 
    # Infinite loop 
    while(True):  
        # reading each frame  
        ret,frame = camera.read()  
 
        if ret:  
            file_name = 'frame' + str(current_frame) + '.png' 
             
            # writing the extracted images  
            cv2.imwrite(file_name, frame)  
 
            # Increase the current frame value  
            current_frame += 1 
        else:  
            break 
 
    camera.release()  
    cv2.destroyAllWindows()  
 
  
def images_to_gif(): 
    # Frame List 
    frames = [] 
 
    images = glob.glob("*.png") 
 
    for image in images: 
     
        new_frame = Image.open(image) 
        extrema = new_frame.convert("L").getextrema()
        if extrema != (0, 0):
    # all black
            frames.append(new_frame) 
    print(len(frames))  
    # Save into a GIF file that loops forever 
    frames[0].save('ana.gif', format='GIF', 
                   append_images=frames[1:150], 
                   save_all=True, 
                   duration=250, loop=150) 
 
def delete_all_images(): 
    # Iterate through all images 
    for i in os.listdir(): 
        if ".png" in i: 
            # remove file 
            os.remove(i) 
 
 
if __name__ == '__main__': 
    convert_video_into_images("ana.mp4") 
    #images_to_gif() 
    #delete_all_images() 