def get_token():
    '''
    Returns token for Microsoft Azure Marketplace Oauth
    Token is good for 10 minutes
    '''
    
    url_args = {
        'client_id': 'Smart-Scale-1',
        'client_secret': 'b50eae37-5263-4693-81d6-9d7c04bc8872',
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'
    }
    
    oauth_url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
    oauth_key = '7d2c5a67c24c45ce90fc219a3fae8bf9'
