#names of all the videos and their corresponding channels
SELECT c.channel_name, v.video_title FROM channel_data c 
JOIN playlist_data p ON p.channel_id=c.channel_id
JOIN video_data v ON p.playlist_id=v.playlist_id
 ;

 # channels have the most number of videos, and how many videos do they have
 SELECT channel_name, channel_video_count FROM channel_data WHERE channel_video_count=(SELECT MAX(channel_video_count) FROM channel_data)
 ;
 #  top 10 most viewed videos and their respective channels
 SELECT v.video_title, v.video_view_count, c.channel_name  FROM video_data v
 JOIN playlist_data p ON p.playlist_id=v.playlist_id
 JOIN channel_data c ON p.channel_id=c.channel_id
 ORDER BY v.video_view_count DESC
 LIMIT 1,10
 ;
 #  How many comments were made on each video, and what are their corresponding video names
 SELECT video_title, video_comment_count from video_data
 ;
 #  Which videos have the 5 highest number of likes, and what are their corresponding channel names
 SELECT v.video_title, v.video_like_count, c.channel_name  FROM video_data v
 JOIN playlist_data p ON p.playlist_id=v.playlist_id
 JOIN channel_data c ON p.channel_id=c.channel_id
 ORDER BY v.video_like_count DESC
 LIMIT 1,5
 ;
 #  total number of likes and dislikes for each video, and what are their corresponding video names
  SELECT video_title, video_like_count from video_data ORDER BY video_like_count DESC
;
 #  total number of views for each channel, and what are their corresponding channel names
 SELECT channel_name, channel_view_count FROM channel_data ORDER BY channel_view_count DESC
 ;
 # names of all the channels that have published videos in the year 2022
 SELECT c.channel_name  FROM video_data v
 JOIN playlist_data p ON p.playlist_id=v.playlist_id
 JOIN channel_data c ON p.channel_id=c.channel_id
 WHERE v.video_published_date like '%2022-%' GROUP BY c.channel_name
 ;
 # average duration of all videos in each channel, and what are their corresponding channel names
 SELECT c.channel_name  FROM video_data v
 JOIN playlist_data p ON p.playlist_id=v.playlist_id
 JOIN channel_data c ON p.channel_id=c.channel_id
 ;
 # Which videos have the 5 highest number of comments, and what are their corresponding channel names
  SELECT v.video_title, v.video_comment_count, c.channel_name  FROM video_data v
 JOIN playlist_data p ON p.playlist_id=v.playlist_id
 JOIN channel_data c ON p.channel_id=c.channel_id
 ORDER BY v.video_comment_count DESC
 LIMIT 1,5