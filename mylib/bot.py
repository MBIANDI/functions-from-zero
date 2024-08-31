import wikipedia

def scrape(name="Microsoft", sentences=1):
    result = wikipedia.summary(name, sentences=sentences) 
    return result