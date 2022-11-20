from pytube import YouTube

save_path = "D:/"
link_to_video = "https://www.youtube.com/watch?v=38f6Vp3fO3o"
        
def start(url,path_to_save):
    yt = YouTube(link_to_video)
    video1 = yt.streams.filter(progressive = True, file_extension = "mp4").first()
    try:
        print("Downloading...")
        video1.download(save_path)
        print("Task Completed!")
    except:
        print("Some Error!, Try Again")

start(link_to_video,save_path)
