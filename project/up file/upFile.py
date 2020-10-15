import json
import requests

def main():
    headers = {"Authorization": "Bearer ya29.a0AfH6SMAYCUCCBa5yVKXJ55u94Y6PEkRvfZ2uTUplLOAgCNWKaJLqI0qe-zDkSxAD17WHajYmNoxVX17Aai3lmOz3hsVahxPg1S8PmxnXAiRZ5wyy4IeNRmmlSFMOG-vVBrBspxUUc28ZSALOE81gSrwGObm4pBMkyN8"}
    para = {
        "name": "videos.mp4",
        "parents": ["15II3iF0uC1WTNsQlJWZuvMELpfC03eEv"]
        }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("./videos.mp4", "rb")
        }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
        )    
    print(r.text)
    

main()
