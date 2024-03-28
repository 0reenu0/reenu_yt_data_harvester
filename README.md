**Reenu's YouTube Data Extraction and Analysis using MySQL and Streamlit**

**Introduction**

Reenu's YouTube Data Extraction and Analysis is a project that aims to allow users to access and analyze data from multiple YouTube channels. The project utilizes MySQL and Streamlit to create a user-friendly application that allows users to retrieve, store, and query YouTube channel and video data.

**Project Overview**

The Reenu's YouTube Data Extraction and Analysis project consists of the following components:

Streamlit Application: A user-friendly multi-page UI built using Streamlit library, allowing users to interact with the application and perform data retrieval and analysis tasks.  
YouTube API Integration: Integration with the YouTube API to fetch channel and video data based on the provided channel ID.
SQL Data Warehouse: Migration of data from the data lake to a SQL database, allowing for efficient querying and analysis using SQL queries.
Data Visualization: Presentation of retrieved data using Streamlit's data visualization features, enabling users to analyze the data through charts.

**Technologies Used:**

Python: The programming language used for building the application and scripting tasks.  
Streamlit: A Python library used for creating interactive web applications and data visualizations.  
YouTube API: Google API is used to retrieve channel and video data from YouTube.  
SQL (MySQL): A relational database used as a data warehouse for storing migrated YouTube data.  
SQLAlchemy: A Python library used for SQL database connectivity and interaction.  
Pandas: A data manipulation library used for data processing and analysis.  

**Installation and Setup:**

To run the Reenu's YouTube Data Extraction and Analysis project, follow these steps:  

Install Python: Install the Python programming language on your machine.  
Install Required Libraries: Install the necessary Python libraries using pip or conda package manager. Required libraries include Streamlit, MySQL driver, SQLAlchemy and Pandas.  
Set Up Google API: Set up a Google API project and obtain the necessary API credentials for accessing the YouTube API.  
Configure Database: Set up a MySQL database for storing the data. Execute DDL statements from the youtube_data_db_DDL.sql file.  
Configure Application:   
    1. Replace api_key in yt_data_etl.py with your YouTube API Key  
    2. Replace mysql connection string with your MySQL connection string in yt_data_etl.py and yt_mysql_helper.py  

**Run the Application:** Launch the Streamlit application using the command-line interface.  

**Usage**  
  
Once the project is setup and running, users can access the Streamlit application through a web browser ( default http://localhost:8501/ ).  

**Features** 
  
The Multi-page application will provide a user interface with the following pages:   
Home page- sidebar with page links and introduction to application  
Data Extraction page:  
        1. Enter a YouTube channel ID to retrieve data for that channel cached in DataFrames.  
        2. Migrate cached data for multiple YouTube channels in the MySQL Data warehouse.  
Data Viewer page: Search and retrieve data from the SQL database using various search options.  
Data Insights page:Perform data analysis using the tables and chart visualization displayed on Data Insights page.  

**Future Enhancements**  

Here are some potential future enhancements for the Reenu's YouTube Data Extraction and Analysis project:  

Authentication and User Management: Implement user authentication and management functionality to secure access to the application.  
Scheduled Data Harvesting: Set up automated data harvesting for selected YouTube channels at regular intervals.  
Advanced Search and Filtering: Enhance the search functionality to allow for more advanced search criteria and filtering options.  
Additional Data Sources: Extend the project to support data retrieval from other social media platforms or streaming services.  
Advanced-Data Analysis: Incorporate advanced analytics techniques and machine learning algorithms for deeper insights into YouTube data.  
Export and Reporting: Add features to export data and generate reports in various formats for further analysis and sharing.  

**Conclusion**  
  
Reenu's YouTube Data Extraction and Analysis project provides a powerful tool for retrieving, storing, and analyzing YouTube channel and video data. By leveraging SQL and Streamlit, users can easily access and manipulate YouTube data in a user-friendly interface. The project offers flexibility, scalability, and data visualization capabilities, empowering users to gain insights from the vast amount of YouTube data available.  

**References**  

Streamlit Documentation: https://docs.streamlit.io/  
YouTube API Documentation: https://developers.google.com/youtube  
SQLAlchemy Documentation: https://docs.sqlalchemy.org/  
Python Documentation: https://docs.python.org/  
