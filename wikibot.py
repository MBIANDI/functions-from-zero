import wikipedia

def scrape(name="Microsoft", lenght=1):
    result = wikipedia.summary(name, sentences=lenght) 
    return result

print(scrape("facebook"))