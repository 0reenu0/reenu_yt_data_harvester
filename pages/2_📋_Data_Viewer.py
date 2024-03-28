import streamlit as st
from yt_mysql_helper import *


# Streamlit app code
def main():

    st.set_page_config(page_title="2. Data Viewer", page_icon=":clipboard:")

    st.sidebar.subheader("YouTube Data Viewer")
    
    st.write('''#### View the channel data stored in Data Warehouse: ''')

    db_channel_df = fetch_channel_data()
    selected_channel_name = st.selectbox("Select a channel", db_channel_df['channel_name'])
    selected_channel= db_channel_df[db_channel_df['channel_name'] == selected_channel_name]
    selected_id=selected_channel['channel_id'].to_string(index=False)

    # Option to search and retrieve data from SQL
    search_option = st.selectbox("Search option", ["None","Videos", "Comments"])
    if search_option == "Videos":
        db_videos_df = get_video_data(selected_id)
        st.subheader("Video Data")
        st.dataframe(db_videos_df)

    elif search_option == "Comments":
        db_comment_df = get_comment_data(selected_id)
        st.subheader("Comment Data")
        st.dataframe(db_comment_df)

# Run the Streamlit app
if __name__ == '__main__':
    main()