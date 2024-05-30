from urllib.request import urlopen
import time 

def getloadtime(url):
    """This function takes a user defined url as input and returns the
    time taken to load that url in seconds"""
    
    if "https" in url or "http" in url:
        openthisurl = urlopen(url)
    else:
        openthisurl = urlopen("https://" + url)
    
    starttime = time.time()
    openthisurl.read()
    endtime = time.time()
    openthisurl.close()
    
    timetoload = endtime - starttime
    
    return timetoload

if __name__ == "__main__":
    url = input("Enter the url: ")
    print(f"The time taken to load {url} is {getloadtime(url):.2f} seconds.")
