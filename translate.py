import requests
import json
import urllib

token = 'get this from command line'

def azure_translate(text, from_lang = 'en', to_lang = 'fr'):
    '''
    Constructs json request for Microsoft Azure request
    Args:
        text: string to be translated
        from_lang: string with language code for language text is originally in (defaults to english)
        to_lang: string with language code for language to translate text in to (defaults to french)
    Returns:
        translated_text: string translated in new language
    '''
    
    req = {
        'Authorization': ('Bearer ' + token),
        'text' : text,
        'from' : from_lang,
        'to' : to_lang
    }
    
    
    response = requests.get('https://api.microsofttranslator.com/v2/http.svc', params = req)

def main(token):
    translated_text = azure_translate('hello, how are you doing?')
    print(translated_text.text)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'speech_file', help='/Users/roman/Desktop/audio.raw')
    args = parser.parse_args()
    main(args.speech_file)
    
