from pytube import YouTube

save_path = "D:/"
link_to_video = "https://www.youtube.com/watch?v=38f6Vp3fO3o"

def percent(tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

def progress_function(stream, chunk,file_handle, bytes_remaining):

    size = stream.filesize
    p = 0
    while p <= 100:
        progress = p
        print (str(p)+'%')
        p = percent(bytes_remaining, size)
        
        
def start(url,path_to_save):
    yt = YouTube(link_to_video, on_progress_callback=progress_function)
    video1 = yt.streams.filter(progressive = True, file_extension = "mp4").first()
    try:
        print("Downloading...")
        video1.download(save_path)
        print("Task Completed!")
    except:
        print("Some Error!, Try Again")
        start(url,path_to_save)

start(link_to_video,save_path)
