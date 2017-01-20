##### Microsoft Cognitive Services API Auth #####
    # Token is valid for 10 mins
AZURE_TOKEN=$(curl --data "" 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken?Subscription-Key=7d2c5a67c24c45ce90fc219a3fae8bf9')

python translate.py $AZURE_TOKEN



