# Bad Translator: Implementable branch

Tutorial on how to setup on main branch

HOW TO USE:
 - Assuming you've created a python script in the same folder as ```badtranslator.py```, import BadTranslator using ```import badtranslator```.
 - Parameters: ```badtranslator.translate(libretranslate_url, times_to_translate, text, source_language)```
 - Save to file: ```badtranslator.translateToFile(libretranslate_url, times_to_translate, text, source_language, file_name)

Example:
```
import badtranslator as bt

text = bt.translate('http://localhost:5000/translate', 3, "Hello world", "en")
print(text)

bt.translateToFile('http://localhost:5000/translate', 3, "Hello world", "en", "output.txt")
```

Possible output: ```Hello```
