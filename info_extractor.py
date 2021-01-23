from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import re
import datetime
from datetime import date
import unidecode

class infoExtractor():
    """Takes all of the titles from a youtube playlist"""
    """also gets dates"""

    def __init__(self,dev_key,playlistId):
        self.DEV_KEY = dev_key
        self.PLAYLIST_ID = playlistId

    def fetch(self):
        YT_API_SERVICE_NAME = 'youtube'
        YT_API_VERSION = 'v3'

        youtube = build(YT_API_SERVICE_NAME,
        YT_API_VERSION,
        developerKey=self.DEV_KEY)
        res = youtube.playlistItems().list(
        part="snippet",
        playlistId=self.PLAYLIST_ID,
        maxResults="50"
        ).execute()

        nextPageToken = res.get('nextPageToken')
        while ('nextPageToken' in res):
            nextPage = youtube.playlistItems().list(
            part="snippet",
            playlistId=self.PLAYLIST_ID,
            maxResults="50",
            pageToken=nextPageToken
            ).execute()
            res['items'] = res['items'] + nextPage['items']

            if 'nextPageToken' not in nextPage:
                res.pop('nextPageToken', None)
            else:
                nextPageToken = nextPage['nextPageToken']

        return res

    def applyPatterns(self,title):
        '''applies a series of patterns to titles to cut them down
        Not optimized'''
        ENGLISH_PATTERN = r"[^a-zA-ZéÊÉè'È\süË]"
        SPACE_PATTERN = r'(\s{2,})'
        REFINED_PATTERN = r"(YouTube)?[&]?(twitterRT)?(kmh)?(hi)?(HP)?(EU\s)?(Roma Fiumicino)?"

        result = re.sub(ENGLISH_PATTERN,"",title)
        result = re.sub(SPACE_PATTERN, " ", result)
        result = re.sub(REFINED_PATTERN,"",result)

        if len(result) > 4:
            if result[-2] == " ":
                result = result[:-1].strip()
                return result.lower()
            else:
                return result.strip().lower()

    def grabVidInfo(self):
        '''gets a list of lists of title and date
        ['drink','day'],can be repetitive'''
        l = []
        res = self.fetch()
        items = res['items']
        for i in range(len(items)):
            title = self.applyPatterns(items[i]['snippet']['title'])
            if title!= None:
                #get rid of accent marks
                title = unidecode.unidecode(title)
                date = items[i]['snippet']['publishedAt'].split("T")[0]
                dt_obj = datetime.datetime.strptime(date,'%Y-%m-%d').date()
                day_of_week = dt_obj.strftime('%A').lower()
                l.append([title,day_of_week])

        return l



