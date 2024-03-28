import streamlit as st
from yt_mysql_helper import *

# Streamlit app code
def main():

    st.set_page_config(page_title="3. Data Insights", page_icon=":bar_chart:")

    st.sidebar.subheader("YouTube Data Insights")
   
    if st.button("Channel with the most number of videos "):
            st.table(fetch_highest_no_videos_channel())
    
    if st.button("Top 10 most viewed videos"):
            df=fetch_top_ten_viewed_videos_with_channel()
            st.bar_chart(df,x='channel_name',y='video_view_count',color=["#FFFFFF"])
            st.table(df)
    
    if st.button("Top 5 most liked videos"):
            st.table(fetch_most_liked_videos_per_channel())
    
    if st.button("Total number of likes per video"):
            st.table(fetch_likes_dislikes_per_video())
    
    if st.button("Total number of views for each channel"):
            df=fetch_total_views_per_channel()
            st.bar_chart(df,x='channel_name',y='channel_view_count',color=["#ffaaf0"])
            st.table(df)

    if st.button("Channels that published videos in the year 2022"):
            st.table(fetch_channel_video_published_in_year('2022'))

    if st.button("Channels that published videos in the year 2023"):
            st.table(fetch_channel_video_published_in_year('2023'))

    if st.button("Channels that published videos in the year 2024"):
            st.table(fetch_channel_video_published_in_year('2024'))
            
   # if st.button("Average duration of all videos in each channel"):
          #  st.table(fetch_avg_duration_per_channel())
    
    if st.button("Top 5 videos with highest number of comments"):
            df=fetch_highest_comments_per_channel()
            st.bar_chart(df,x='video_title',y=['video_comment_count'],color=["#ff0"]) #yellow
            st.table(df)

    if st.button("No. of Comments per video"):
            st.table(fetch_comment_count_per_video())

 #  names of all the videos and their corresponding channels
    if st.button("List all video names with channel name "):
            st.table(fetch_videos_per_channel())

# Run the Streamlit app
if __name__ == '__main__':
    main()