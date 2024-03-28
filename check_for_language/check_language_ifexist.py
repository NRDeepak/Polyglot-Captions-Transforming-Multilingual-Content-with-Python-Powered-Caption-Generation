LANGUAGES = {
    'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic',
    'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian',
    'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan',
    'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian',
    'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
    'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish',
    'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian',
    'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole',
    'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew',
    'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic',
    'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian',
    'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh',
    'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz',
    'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian',
    'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay',
    'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi',
    'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali',
    'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian',
    'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian',
    'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian',
    'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala',
    'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish',
    'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik',
    'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish',
    'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek',
    'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish',
    'yo': 'yoruba', 'zu': 'zulu',
}


class check_language:

    def check_lang_if_exists(self, translate_language):
        """
              Checks if user input language exists or not.

              Parameters:
                  translate_language (str): User input language.

              Returns:
                  str: The path to the extracted audio file.
              """
        translate_language = translate_language.lower()
        try:
            keyword = [key for key, value in LANGUAGES.items() if value == translate_language]

            return keyword[0]
        except:
            print("Input language is not present in the list! Please check for spelling errors.")

