import requests, json, random, time

url = 'http://localhost:5000/translate'
languages = ["en", "ar", "az", "ca", "zh", "cs", "da", "nl", "eo", "fi", "fr", "de", "el", "he", "hi", "hu", "id", "ga", "it", "ja"]

source = "de"

#source = input("What language is your text coming from? (Default: German)")
times = int(input("\n\n\nHow many times do you want to translate your text?     "))
text = input("Insert your text:                                      ")

if not isinstance(times, int) and times >= 1:
    raise Exception("The number of times has to be a number > or = 1")
elif not isinstance(text, str):
    raise Exception("The text has to be a string!")

progress = int(round(30/times))
percentage = int(round(100/times, 1))

start = time.time()
translation_start = time.time()

if source is None:
    source = "de"

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
measured_time = time.time() - translation_start

missing = 30-progress

print("\n\n\n1 - Translating from de to", lang1, "-", round(measured_time, 2), "s [", progress*"#", missing*"-", "] -", percentage, "%")

for i in range(0, times-1):
    translation_start = time.time()
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
    measured_time = time.time() - translation_start
    
    missing = 30-(i+2)*progress
    print(i+2, "- Translating from", lang1, "to", lang2, "-", round(measured_time, 2), "s [", (i+2)*progress*"#", missing*"-", "] -", percentage+percentage*(i+1), "%")

print("\nTranslating back to source:", source)
translation_start = time.time()

request = {
		'q': translation,
		'source': lang2,
		'target': source,
		'format': "text",
		'api_key': ""
	}

translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]
measured_time = time.time() - translation_start
print("    Translating from", lang2, "to de -", round(measured_time, 2), "s")

stop = time.time() - start
print("\nFinal result in", round(stop, 2), "s:\n", translation)

save = input("\nDo you want to save the file? (y/n) ")

if save == "y":
    name = input("Enter file name:                    ")

    file = open(name, "w")
    file.write(translation)
    file.close()

    print("Saved!")
elif save == "n":
    pass
else:
    while save is not "y" or "n":
        save = input("Type 'y' for yes or 'n' for no:     ")
        if save is "y":
            name = input("Enter file name:                    ")
    
            file = open(name, "w")
            file.write(translation)
            file.close()

            print("Saved!")
            pass
        if save is "n":
            pass
