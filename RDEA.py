import streamlit as st

# Streamlit app code
def main():
    st.set_page_config(
        page_title="Home",
        page_icon="👋",
    )

    st.write("# Welcome to Reenu's D.E.A Application! 👋")

    st.sidebar.success("Click a page link above.")

    st.markdown(
        """
        R.D.E.A- Reenu's Youtube Data Extractor and Analysis is an app to extract data from youtube Channels and view insights on the same.
        #### **👈 Click on the page links on the sidebar to navigate** 

        #### Want to learn more about the links?
            1. The Data Extractor page allows to perform extraction by providing a Youtube Channel Id and provides capability to upload it to a Data Warehouse.
            2. The Data Viewer page provides options to view data uploaded in the Data Warehouse.
            3. The Data Insights page provides Insights on the data uploaded in the Data Warehouse.
        """)


# Run the Streamlit app
if __name__ == '__main__':
    main()