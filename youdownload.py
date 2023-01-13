from pytube import YouTube

def download(link):
    you = YouTube(link)
    you = you.streams.get_highest_resolution()

    try:
        you.download()
    except:
        print("something wrong")
    print("downloaded successfully")

link = input("Enter the link --> ")
download(link)

