from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "rock-groove-382223",
  "private_key_id": "77d1d6287775884aa50700f2d984b1d99834676c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCxzkLyGLUPiPH5\nApzF4R33OLwxWI8NqlTp3IlUJ9BGJ+etzpFnHzgn5uRQh5oKme1DPTQ8/W2V7xQa\nuNAIozUOLbpNMPPASvLfFZ3FWwL4fntbSkaDdzMktXsMZwavdY1MGPUP29KT7zqn\n/XPuESiS2iYIj2j4yGCwMUffA64YghoeN9ITfC/sIDOK+clvZRq5zYi1ubzy4ZSm\nm3cuiamJB6/zqS8JYpkhjNp36pCR8mDJQ4uurQ8P8KW5OZ68aujHmPsQhE4DwGwS\nLkol99WtWnydVWJQEC2wClTB15Q70WfpPzlmqeLZd0rsscjLKKzqPSTVN80NxAZA\nw3HLvrL1AgMBAAECggEAD1wKBxqAnumYPYfZkx5x6uaecITTQWhIEuECMUrfKwWi\nIIQ0+1DZwQNTuxZ7sBQWnYsD9Yt5k/d7J8kfRMppzY0VsuVaU8TQW4UP2U9AtRv3\n/ALb5IS/iO7vGjssJgFkRgFB6i91xAxpEhSgQch/AMXnfdslmO12V2y/u1F4uz/H\nskjBBacFyPmWncNRfcEyu7q1ZMZU4NW7TqD2BodAdXV3bP/YvKE4Q5LE96zm3eps\nHB9z7LmH6tqnMOx2bsx8eDDsiqQdmOv0+P+KNQlt8opUtFDfdArTh+CArLxuavNp\n423y3rHC0wyXIyuaX2SoM7diT9lFtYHdq8cYgPEEYQKBgQDbASnOyFkTwEKTwTIc\nVFveqDDRzq7/TzUNZ0YubQlcYKK+Vx3DdfMyyEHU3ZAAS0rkT26bzSNCaouzmoci\nI58vH45eBY81BtMwf1z8gQiL8v/2o5eBRaZvCpnTzUYEyZ/2Jr8IzbfXYcCuSIo1\nSczj3ha7rQmGLIxXAqs6ihkS6wKBgQDP13UVVSTDa+yYV2D454uvPrSo8CiSJWzL\nD0Ssn2Df79BIrqpFgpXi0OVYVWptDwG2TSzXNqpEjK3OgabwkmS4HlTrn3y+cVcz\nZBFt/rna2izbK0puJJjpkpEJVxiXrHkX+hjtGgCRGTOt5UREBob5BeX8yVw1kiIy\ni2oj1zkZnwKBgQDMGptyIfoSlD34Ijene19bdXh6MJubSaBx62vW3Lu6oj1KEzqj\n7YtIKqZf0lXgUEtt2DGHdnmD7nRgYIXMZVJ3wnsWWSwMCV5NdoWctkzW0ROIMxKB\n4f2ow0J1yHuW/qnb6GRlugO58Vp3kxdrbmpLe7HIGw4jQ+VPOieGmSmhHQKBgHh2\n19zacal2xzXxBzqc8eBLxuhX8hvq5yi2m8Y1xi9lTuKhof0R2BATpapSL5IwbXyd\nNI00mPGMXDzh9sFfCFOS+QNseB/lj3Yw3M1VI6HObMtHRyeZvKs8kSXJvm5CwBj+\nky3xsTxoUATNaojHA7oYCho/F1vRbFLBbW6CkwzfAoGBAK8CS6TB80jNrjP94WA7\nVzm8ymjTuSTR/W6ZRtPHJKbBns16JFg02iDbg0ka9fY/sXPYitLgEGW++DdAjJ3p\nlAzkG3FQxk0LJFensLHQfq2QPnpegjH4cLagFGG5JYsKTLySockKtFO2aRawZ5tK\n9duf4WXwlQLiR2gBQpme1Em0\n-----END PRIVATE KEY-----\n",
  "client_email": "172126273131-compute@developer.gserviceaccount.com",
  "client_id": "118360923701836878557",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/172126273131-compute%40developer.gserviceaccount.com"
}

try:
    res = requests.get(
        f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    
    print("Loading...")

    soup = BeautifulSoup(res.text, 'html.parser')

    info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()

    print(info)
    
    credentials = service_account.Credentials.from_service_account_info(credentials_dict)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket('python_gitactions')
    blob = bucket.blob('weather_info_actions.txt')
    
    blob.upload_from_string(info + '\n')
    
    print("File Uploaded")
        
    print("Finished.")
    
except Exception as ex:
    print(ex)