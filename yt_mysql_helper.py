import pandas as pd
import mysql.connector as sql
from sqlalchemy import create_engine,text


# Connect to the MySQL database
#replace username, password, portno  and dbname according to your MySQL user creds, port configuration and schema name
connection_string = 'mysql+pymysql://username:password@localhost:portno/schemaname'
engine = create_engine(connection_string)

# Function to retrieve channel data from MySQL
def fetch_channel_data():
    query = "SELECT * FROM channel_data"
    df = pd.read_sql(query, engine)
    return df

# Function to retrieve video data from MySQL
def fetch_video_data(channelId):
    query = text("SELECT * FROM video_data where playlist_id in (Select playlist_id from playlist_data where channel_id =:channel_id)")
    parameters={}
    parameters['channel_id'] = channelId
    df = pd.read_sql(query, engine, params=parameters)
    return df

# Function to retrieve comment data from MySQL
def fetch_comment_data(channelId):
    query = text(''' SELECT * FROM comments where video_id in (SELECT video_id FROM video_data where playlist_id in 
    (Select playlist_id from playlist_data where channel_id = :channel_id))''')
    parameters={}
    parameters['channel_id'] = channelId
    df = pd.read_sql(query, engine, params=parameters)
    return df

 #  names of all the videos and their corresponding channels
def fetch_videos_per_channel():
    query = text(''' SELECT c.channel_name, v.video_title FROM channel_data c 
                    JOIN playlist_data p ON p.channel_id=c.channel_id
                    JOIN video_data v ON p.playlist_id=v.playlist_id''')
    df = pd.read_sql(query, engine)
    return df

 #  channel which have the most number of videos
def fetch_highest_no_videos_channel():
    query = text('''  SELECT channel_name, channel_video_count FROM channel_data WHERE channel_video_count=(SELECT MAX(channel_video_count) 
                      FROM channel_data)''')
    df = pd.read_sql(query, engine)
    return df

 #  top 10 most viewed videos and their respective channels
def fetch_top_ten_viewed_videos_per_channel():
    query = text('''    SELECT v.video_title, v.video_view_count, c.channel_name  FROM video_data v
                        JOIN playlist_data p ON p.playlist_id=v.playlist_id
                        JOIN channel_data c ON p.channel_id=c.channel_id
                        ORDER BY v.video_view_count DESC
                        LIMIT 1,10''')
    df = pd.read_sql(query, engine)
    return df

 #  How many comments were made on each video, and what are their corresponding video names
def fetch_comment_count_per_video():
    query = text('''  SELECT video_title, video_comment_count from video_data   ''')
    df = pd.read_sql(query, engine)
    return df

 #  Which videos have the 5 highest number of likes, and what are their corresponding channel names
def fetch_most_liked_videos_per_channel():
    query = text('''    SELECT v.video_title, v.video_like_count, c.channel_name  FROM video_data v
                        JOIN playlist_data p ON p.playlist_id=v.playlist_id
                        JOIN channel_data c ON p.channel_id=c.channel_id
                        ORDER BY v.video_like_count DESC
                        LIMIT 1,5  ''')
    df = pd.read_sql(query, engine)
    return df

 #  total number of likes and dislikes for each video, and what are their corresponding video names
def fetch_likes_dislikes_per_video():
    query = text('''   SELECT video_title, video_like_count from video_data ORDER BY video_like_count DESC ''')
    df = pd.read_sql(query, engine)
    return df

 #  total number of views for each channel, and what are their corresponding channel names
def fetch_total_views_per_channel():
    query = text('''    SELECT channel_name, channel_view_count FROM channel_data ORDER BY channel_view_count DESC ''')
    df = pd.read_sql(query, engine)
    return df

 #  names of all the channels that have published videos in the year 2022
def fetch_channel_video_published_in_year(year):
    query = text('''    SELECT c.channel_name  FROM video_data v
                        JOIN playlist_data p ON p.playlist_id=v.playlist_id
                        JOIN channel_data c ON p.channel_id=c.channel_id
                        WHERE v.video_published_date like :year GROUP BY c.channel_name ''')
    parameters={}
    parameters['year'] = '%'+year+'-%'         
    df = pd.read_sql(query, engine,params=parameters)
    return df

 #  average duration of all videos in each channel, and what are their corresponding channel names
def fetch_avg_duration_per_channel():
    query = text('''    SELECT c.channel_name  FROM video_data v
                        JOIN playlist_data p ON p.playlist_id=v.playlist_id
                        JOIN channel_data c ON p.channel_id=c.channel_id
                        ''')
    df = pd.read_sql(query, engine)
    return df

 #  Which videos have the 5 highest number of comments, and what are their corresponding channel names
def fetch_highest_comments_per_channel():
    query = text('''    SELECT v.video_title, v.video_comment_count, c.channel_name  FROM video_data v
                        JOIN playlist_data p ON p.playlist_id=v.playlist_id
                        JOIN channel_data c ON p.channel_id=c.channel_id
                        ORDER BY v.video_comment_count DESC
                        LIMIT 1,5   ''')
    df = pd.read_sql(query, engine)
    return df