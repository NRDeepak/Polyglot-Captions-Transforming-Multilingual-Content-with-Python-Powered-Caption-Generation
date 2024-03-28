from googletrans import Translator

translator = Translator()


class translate_text_class:
    def translate_text(self, input_text, translate_language):
        translation = translator.translate(input_text, dest=translate_language)
        return translation.text
