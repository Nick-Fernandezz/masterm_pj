

def findVideoFrame(url: str) -> str:
    id = url.split('/')[-1]
    return f'https://www.youtube.com/embed/{id}'
        

