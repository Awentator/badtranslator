#BadTranslator - interactive branch. By Awentator. Version: 24.03.2023
#Repository (report issues): https://github.com/Awentator/badtranslator/
import requests, json, random, time

#Change url to LibreTranslate server and append '/translate'
url = 'http://localhost:5000/translate'

#Every LibreTranslate supported language
languages = ["en", "ar", "az", "ca", "zh", "cs", "da", "nl", "eo", "fi", "fr", "de", "el", "he", "hi", "hu", "id", "ga", "it", "ja"]

#Input information
source = input("\n\n\nWhat language is your text coming from?                   ")
times = int(input("How many times do you want to translate your text?        "))
readfromfile = input("Do you want to insert the text or read from file? (i/r)   ")

#If text should be imported from a file
if readfromfile == "r":
    #Ask for file name, open and read it
    name = input ("What is the file's name? ")
    file = open(name, "r")
    text = file.read()
elif readfromfile == "i":
    #Insert the text
    text = input("Insert your text:                                         ")
else:
    while readfromfile != "r" or "i":
        #Ask for every time no valid input is given
        readfromfile = input("Type 'r' to read from file or 'i' to directly insert your text: ")
        if readfromfile == "r":
            #Ask for file name, open and read it
            name = input ("What is the file's name? ")
            file = open(name, "r")
            text = file.read()
            break
        elif readfromfile == "i":
            #Insert the text
            text = input("Insert your text:                                         ")
            break

#Search for errors and throw exceptions
if not isinstance(times, int) and times >= 1:
    raise Exception("The number of times has to be a number > or = 1")
elif not isinstance(text, str):
    raise Exception("The text has to be a string!")

#Progress and percentage for progress bar
progress = int(round(30/times))
percentage = int(round(100/times, 1))

#Time measurement
start = time.time()
translation_start = time.time()

#Set random languages for first translation
lang1 = random.choice(languages)
lang2 = random.choice(languages)

#Server API request
request = {
	'q': text,
	'source': source,
	'target': lang1,
	'format': "text",
	'api_key': ""
}

#Send API request
translation = json.loads(str(requests.post(url, json = request).text))["translatedText"]

#Calculate progress bar, prints status output
measured_time = time.time() - translation_start
missing = 30-progress
print("\n\n\n1 - Translating from de to", lang1, "-", round(measured_time, 2), "s [", progress*"#", missing*"-", "] -", percentage, "%")

#Main loop for every random translation
for i in range(0, times-1):
    #Time measurement of current translation
    translation_start = time.time()

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
    
    #Calculate progress bar, prints status output
    measured_time = time.time() - translation_start
    missing = 30-(i+2)*progress
    print(i+2, "- Translating from", lang1, "to", lang2, "-", round(measured_time, 2), "s [", (i+2)*progress*"#", missing*"-", "] -", percentage+percentage*(i+1), "%")

#Final output back to source
print("\nTranslating back to source:", source)
translation_start = time.time()

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

#Final translation, calculates time
measured_time = time.time() - translation_start
print("    Translating from", lang2, "to de -", round(measured_time, 2), "s")

#Final stats message, displays file output
stop = time.time() - start
print("\nFinal result in", round(stop, 2), "s (average", round((stop/(times+2)), 2), "s):\n", translation)

#Optional: Save to file
save = input("\nDo you want to save the file? (y/n) ")

#If file should be saved: yes
if save == "y":
    #Enter name of file
    name = input("Enter file name:                    ")

    #Open the file, write and close it
    file = open(name, "w")
    file.write(translation)
    file.close()

    print("Saved!")
#If file should be saved: no
elif save == "n":
    #Proceed/ignore if translation should not be saved
    pass
else:
    #Ask for every time no valid input is given
    while save != "y" or "n":
        #Print and ask for correct answer
        save = input("Type 'y' for yes or 'n' for no:     ")
        #If file should be saved: yes
        if save == "y":
            #Enter name of file
            name = input("Enter file name:                    ")

            #Open the file, write and close it
            file = open(name, "w")
            file.write(translation)
            file.close()

            print("Saved!")
            break
        #If file should be saved: no
        elif save == "n":
            #Proceed/ignore if file should not be saved
            break
