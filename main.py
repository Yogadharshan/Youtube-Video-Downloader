# importing the module 
import pytube 
  
# where to save 
SAVE_PATH = "D:/" #to_do 
  
# link of the video to be downloaded 
link="https://www.youtube.com/watch?v=JT80XhYJdBw"
  
try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = (pytube.YouTube(link)).streams
except: 
    print("Connection Error") #to handle exception 
  
# filters out all the files with "mp4" extension 
mp4files = yt.filter(res="720p",mime_type="video/mp4").first() 
    
  
# get the video with the extension and
# resolution passed in the get() function 
 
try: 
    # downloading the video 
    mp4files.download(SAVE_PATH)
    print("Downloading...") 
except: 
    print("Some Error!") 
print('Task Completed!')