#!/usr/bin/env python
# coding: utf-8


from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
from sqlalchemy import create_engine,text
import mysql.connector as sql


api_key='---- Replace with your YouTube API key ----'

channel_ids_default_list=['--- channel_id----','---channel id---' ]

youtube=build('youtube','v3',developerKey=api_key)


def get_channel_stats(yt,channel_ids):
    all_data=[]
    req=yt.channels().list(
        part='id,snippet,statistics,status,contentDetails',
        id=','.join(channel_ids))
    res=req.execute()
    
    for item in res['items']:
        data=dict( channel_id=item['id'],
                   channel_name=item['snippet']['title'],
                   channel_type='youtube#channel',
                   channel_description=item['snippet']['description'],
                   channel_subscriber_count=item['statistics']['subscriberCount'],
                   channel_view_count=item['statistics']['viewCount'],
                   channel_video_count=item['statistics']['videoCount'],
                   channel_status=item['status']['privacyStatus'],
                   playlist_id=item['contentDetails']['relatedPlaylists']['uploads'] 
                 )
         
        all_data.append(data)
    return all_data
    


# In[4]:


def get_playlist_info(yt,playlist_id):

    next_page_token = None
    playlist_data=[]
    
    while True:
        playlist_res=yt.playlists().list(
            part='snippet',
            id=playlist_id,
            maxResults=50,
        pageToken=next_page_token).execute()
    
        playlist=playlist_res['items']
        for pl in playlist:
                data=dict(channel_id=pl['snippet']['channelId'],
                         playlist_id=playlist_id,
                         playlist_name=pl['snippet']['title'])    
                playlist_data.append(data)
            
        next_page_token = playlist_res.get('nextPageToken')

        if next_page_token is None:
            break
    return playlist_data


# In[5]:


def get_playlist_videoIds(yt, playlist_id):
    next_page_token = None

    videoIds=[]

    while True:
        playlistItem_res=yt.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
        ).execute()
        
        playlists=playlistItem_res['items']
        for playlistItem in playlists:
            videoIds.append(playlistItem['contentDetails']['videoId'])

        next_page_token = playlistItem_res.get('nextPageToken')
        if next_page_token is None:
            break
        return videoIds


# In[6]:


def get_video_stats(yt,playlist_id):

    videoIds=get_playlist_videoIds(yt,playlist_id)
            
    video_res=yt.videos().list(
    part='id,snippet,contentDetails,statistics',
    id=','.join(videoIds),
    maxResults=50).execute()

    videos=video_res['items']
    video_data=[]
    for video in videos:
        data=dict( playlist_id=playlist_id,
                  video_id=video['id'],
                  video_title=video['snippet']['title'],
                  video_description=video['snippet']['description'],
                  video_published_date=video['snippet']['publishedAt'],
                  video_view_count=video['statistics']['viewCount'],
                  video_like_count=video['statistics']['likeCount'],
                  video_dislike_count=0, #private property as on and after dec13, 2021, only channel owner can access
                  video_favorite_count=0,#deprecated in 2015, always 0
                  video_comment_count= video['statistics']['commentCount'],
                  video_duration=video['contentDetails']['duration'],
                  video_thumbnail=video['snippet']['thumbnails']['default']['url'], # valid thumbnail key values are, default,standard, high,medium,maxres
                  caption_status=video['contentDetails']['caption']        
        )
        video_data.append(data)
        
    return video_data



def get_video_comments_data(yt,video_id):
   
    comments_res=yt.commentThreads().list(
    part='id,snippet',
    videoId=video_id,
    maxResults=50
    ).execute()

    comments=comments_res['items']
    comments_data=[]
    for comment in comments:
        comment=dict(
            video_id=comment['snippet']['videoId'],
            comment_id=comment['id'],
            comment_text=comment['snippet']['topLevelComment']['snippet']['textDisplay'],
            comment_author=comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
            comment_published_date=comment['snippet']['topLevelComment']['snippet']['publishedAt']
        )
        comments_data.append(comment)
    return comments_data


# In[11]:


def get_all_comments_data(yt,channelId):

    next_page_token=None
    comments_res=yt.commentThreads().list(
    part='id,snippet',
    #videoId=video_id,
    allThreadsRelatedToChannelId=channelId,
    maxResults=50,
    pageToken=next_page_token
    ).execute()
    
    while True:
        comments=comments_res['items']
        comments_data=[]
        for comment in comments:
            comment=dict(
                video_id=comment['snippet']['videoId'],
                channel_id=channelId,
                comment_id=comment['id'],
                comment_text=comment['snippet']['topLevelComment']['snippet']['textDisplay'],
                comment_author=comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                comment_published_date=comment['snippet']['topLevelComment']['snippet']['publishedAt']
            )
            comments_data.append(comment)
        next_page_token=comments_res.get('nextPageToken')
        if next_page_token is None:
            break
        else:
            print("next comment page")
    return comments_data




def get_channel_data(channel_id):
    channel_ids=[channel_id]
    global video_df
    global comments_df
    global ch_df
    global playlist_df
    ch_stats=get_channel_stats(youtube,channel_ids)
    ch_df=pd.DataFrame(ch_stats)
    
    comments_data=[]
    
    pl_id=ch_df.iloc[0]['playlist_id']
    playlist_info= get_playlist_info(youtube,pl_id)
    video_data= get_video_stats(youtube,pl_id)
    video_df=pd.DataFrame(video_data)

    video_df = video_df.reset_index() 
    for index, row in video_df.iterrows():
       comments_data.extend(get_video_comments_data(youtube,row['video_id'])) #not recommended to iterate over dataframes as it increases memory usage
        
    playlist_df=pd.DataFrame(playlist_info)
    comments_df=pd.DataFrame(comments_data)

    print('retrieved comments count:',len(comments_data))
    print('retrieved video count:',len(video_data))
    print('retrieved playlist count:',len(ch_stats))
    return video_data    


# In[16]:


def get_channel_data_full(channel_id):

    channel_ids=[channel_id]

    global video_df
    global comments_df
    global ch_df
    global playlist_df

    global video_data
    global comments_data
    global ch_stats
    global playlist_info

    ch_stats=get_channel_stats(youtube,channel_ids)
    ch_df=pd.DataFrame(ch_stats)
    
    comments_data=[]

    pl_id=ch_df.iloc[0]['playlist_id']
    playlist_info= get_playlist_info(youtube,pl_id)

    print('retrieved playlist count:',len(playlist_info)) 

    video_data= get_video_stats(youtube,pl_id)
   
    print('retrieved video count:',len(video_data))

    comments_data=get_all_comments_data(youtube,channel_id) 

    print('retrieved comments count:',len(comments_data))

    ch_df=pd.DataFrame(ch_stats)
    playlist_df=pd.DataFrame(playlist_info)
    video_df=pd.DataFrame(video_data)
    comments_df=pd.DataFrame(comments_data)
    return      




# Migrate channel data to SQL
def insert_to_mysqldb():

    #replace username, password, portno  and dbname according to your MySQL user creds, port configuration and schema name
    connection_string = 'mysql+pymysql://username:password@localhost:portno/schemaname'

    engine = create_engine(connection_string)

    with engine.begin() as conn:
        channel_name=ch_df['channel_name']
        ch_df1 = ch_df.drop(['playlist_id'],axis=1)
        video_df1 = video_df.drop(['index'],axis=1)

        ch_df1.to_sql('channel_data', conn, if_exists='append', index=False)
        playlist_df.to_sql('playlist_data', conn, if_exists='append', index=False)
        video_df1.to_sql('video_data', conn, if_exists='append', index=False)
        comments_df.to_sql('comments', conn, if_exists='append', index=False)

    return channel_name




