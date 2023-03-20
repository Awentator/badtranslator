import requests, json, random

url = 'http://localhost:5000/translate'
languages = ["en", "ar", "az", "ca", "zh", "cs", "da", "nl", "eo", "fi", "fr", "de", "el", "he", "hi", "hu", "id", "ga", "it", "ja"]

source = "de"
output = "de"

#source = input("What language is your text coming from? (Default: German)")
#output = input("What language should your text be? (Default: German)")
times = int(input("How many times do you want to translate your text? "))
text = input("Insert your text: ")

if source is None:
    source = "de"
if output is None:
    output = "de"

lang1 = random.choice(languages)
lang2 = random.choice(languages)

request = {
	'q': text,
	'source': source,
	'target': lang1,
	'format': "text",
	'api_key': ""
}

print("\n\n\n# 0 : Translating from de to ", lang1)
translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]

for i in range(0, times):
    if i >= 1:
        lang1 = lang2
    lang2 = random.choice(languages)

    request = {
		'q': translation,
		'source': lang1,
		'target': lang2,
		'format': "text",
		'api_key': ""
	}
    
    print("#", i+1, ": Translating from ", lang1, "to ", lang2)
    translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]

request = {
		'q': translation,
		'source': lang2,
		'target': output,
		'format': "text",
		'api_key': ""
	}

print("Translating from ", lang2, "to de")
translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]

print("\nFinal result:\n", translation)