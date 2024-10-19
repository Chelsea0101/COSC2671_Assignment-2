"""
COSC2671 Social Media and Network Analytics
@author Jeffrey Chan, RMIT University, 2023

"""

import re
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

class RedditProcessing:
    """
    This class is used to pre-process Reddit posts.  This centralises the processing to one location.  Feel free to add or edit.
    """

    def __init__(self, tokeniser, lStopwords):
        """
        Initialise the tokeniser and set of stopwords to use.

        @param tokeniser:
        @param lStopwords:
        """

        self.tokeniser = tokeniser
        self.lStopwords = lStopwords



    def process(self, text, language = 'en'):
        """
        Perform the processing.
        @param text: the text (tweet) to process

        @returns: list of (valid) tokens in text
        """
            # Detect language and only proceed if the text is in the target language
        try:
            detected_language = detect(text)
        except:
            return []  # Return empty list if language detection fails
    
        if detected_language != language:
            return []  # Return empty list if the text is not in the target language

        text = text.lower()
        tokens = self.tokeniser.tokenize(text)
        tokensStripped = [tok.strip() for tok in tokens]

        # pattern for digits
        # the list comprehension in return statement essentially remove all strings of digits or fractions, e.g., 6.15
        regexDigit = re.compile(r"^\d+\s|\s\d+\s|\s\d+$")
        # regex pattern for http
        regexHttp = re.compile("^http")
        # Pattern to match GIF references (either [GIF] or .gif URLs)
        regexGif = re.compile(r"\[gif\]", re.IGNORECASE)  # matches "[GIF]" (case-insensitive)
        regexGifUrl = re.compile(r"https?://\S+\.gif", re.IGNORECASE)  # matches URLs ending in ".gif"

        return [tok for tok in tokensStripped if tok not in self.lStopwords and regexDigit.match(tok) == None and regexHttp.match(tok) == None and regexGif.match(tok) is None and regexGifUrl.match(tok) is None]