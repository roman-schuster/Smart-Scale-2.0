token = 'test'
# gotten from command line arg - token will be a base 64 encoded plain-text file

txt = 'here, have some text'
to_lang = 'fr'

translation_request = {
    'appid' : ('Bearer ' + token),
    'text' : txt,
    'from' : 'en',
    'to' : to_lang,
}
