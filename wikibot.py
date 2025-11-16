import wikipedia 
result = wikipedia.summary("facebook", sentences=10)
print(result)

def scrape(name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=length)
    return result

print(scrape("Wikipedia"))
