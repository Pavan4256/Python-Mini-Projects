import pafy
url="Enter url here"    
video=pafy.new(url)
# get best resolution of the video
best=video.getbest()
# best resolution in required format[give your req format in "preftype"]
best = video.getbest(preftype="mp4")
#if you want to specify a particular path for the video
filename = best.download(filepath="Path to download")
