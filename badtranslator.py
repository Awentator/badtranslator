#BadTranslator - implementable branch. By Awentator. Version: 22.03.2023
#Repository (report issues): https://github.com/Awentator/badtranslator/
import requests, json, random

#Standard translate method
def translate(url, times, text, source):
    #Return error message if no valid input is provided
    if isinstance(url, str) or isinstance(times, int) or isinstance(text, str) or isinstance(source, str):
        raise TypeError("Invalid input")
    
    #Every LibreTranslate supported language
    languages = ["en", "ar", "az", "ca", "zh", "cs", "da", "nl", "eo", "fi", "fr", "de", "el", "he", "hi", "hu", "id", "ga", "it", "ja"]

    #Set random languages for first translation
    lang1 = random.choice(languages)
    lang2 = random.choice(languages)

    #API request
    request = {
        'q': text,
        'source': source,
        'target': lang1,
        'format': "text",
        'api_key': ""
    }

    #Send API request
    translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]

    #Main loop for every random translation
    for i in range(0, times-1):
        #Run at second loop
        if i >= 1:
            lang1 = lang2
        
        #Set new target language as long as it differents from current source language
        lang2 = random.choice(languages)
        while lang2 == lang1:
            lang2 = random.choice(languages)

        #API request     
        request = {
            'q': translation,
            'source': lang1,
            'target': lang2,
            'format': "text",
            'api_key': ""
        }

        #Send API request      
        translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]
        
    #API request
    request = {
            'q': translation,
            'source': lang2,
            'target': source,
            'format': "text",
            'api_key': ""
        }

    #Send API request       
    translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]

    #Return result
    return translation

#Translate method, outputs translation to file
def translateToFile(url, times, text, source, filename):
    #Translate
    translation = translate(url, times, text, source)

    #Open, write and close file
    file = open(filename, "w")
    file.write(translation)
    file.close()
