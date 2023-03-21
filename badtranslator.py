import requests, json, random
def translate(url, times, text, source):
    languages = ["en", "ar", "az", "ca", "zh", "cs", "da", "nl", "eo", "fi", "fr", "de", "el", "he", "hi", "hu", "id", "ga", "it", "ja"]

    lang1 = random.choice(languages)
    lang2 = random.choice(languages)

    request = {
        'q': text,
        'source': source,
        'target': lang1,
        'format': "text",
        'api_key': ""
    }

    translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]

    for i in range(0, times-1):
        if i >= 1:
            lang1 = lang2
        lang2 = random.choice(languages)
        while lang2 == lang1:
            lang2 = random.choice(languages)
                
        request = {
            'q': translation,
            'source': lang1,
            'target': lang2,
            'format': "text",
            'api_key': ""
        }
                
        translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]

        request = {
                'q': translation,
                'source': lang2,
                'target': source,
                'format': "text",
                'api_key': ""
            }
            
        translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]

        return translation
