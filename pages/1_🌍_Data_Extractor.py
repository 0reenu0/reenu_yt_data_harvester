import streamlit as st
from yt_data_etl import get_channel_data,insert_to_mysqldb


# Streamlit app code
def main():

    st.set_page_config(page_title="1. Data Extractor", page_icon=":globe_with_meridians:")

    st.subheader("Extracted Data will display here!")

    st.sidebar.subheader("YouTube Data Extraction")
    
    channel_id_txt= st.sidebar.text_input("Enter a youtube channel id: ", key="channel_id")

    if st.sidebar.button("Pull Data"):
         result_list=get_channel_data(channel_id_txt)
         st.write(*result_list)
  
    if st.sidebar.button("Migrate to SQL"):
        channel_name=insert_to_mysqldb()
        st.success(f"Data for channel '{channel_name[0]}' migrated to SQL successfully.")

# Run the Streamlit app
if __name__ == '__main__':
    main()