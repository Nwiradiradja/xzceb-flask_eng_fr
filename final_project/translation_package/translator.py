from deep_translator import MyMemoryTranslator

en_translator = MyMemoryTranslator(source='fr', target='en')
fr_translator = MyMemoryTranslator(source='en', target='fr')


def english_to_french(text):
    translation = fr_translator.translate(text)
    return translation


def french_to_english(text):
    translation = en_translator.translate(text)
    return translation
