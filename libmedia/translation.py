from translate import Translator

def translate(text):
    translator = Translator(from_lang='en', to_lang='ru')
    res = translator.translate(text)
    # print(res)
    return res