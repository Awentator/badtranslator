# Bad Translator
A very bad translator for creating funny texts based on LibreTranslate. Translates a text x times into a random language.

Also see implementable branch for implementing to your code!

HOW TO SETUP:
1. Download and intall the Docker Daemon. See https://docs.docker.com/get-docker/
2. Install python with ```sudo apt-get install python3```
3. Setup LibreTranslate using CLI:
   - ```docker run -ti -p 5000:5000 libretranslate/libretranslate```
   - Depending on your internet connection, it might take 5-15 minutes to download all the languages.
4. Run my code with ```python3 badtranslator.py```

Optional: It may be easier installing git with ```sudo apt-get install git-all``` and running ```git clone https://github.com/awentator/badtranslator```. Then cd into your folder with ```cd badtranslator```.
(For further information, see https://github.com/git-guides/install-git)

Enjoy! Feature requests are always welcome!
