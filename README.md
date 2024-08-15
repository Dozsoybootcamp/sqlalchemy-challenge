SQLAlchemy Climate Analysis
Project Overview
This project is part of the SQLAlchemy challenge, where the goal is to analyze and explore climate data from the hawaii.sqlite database. The analysis includes precipitation and station analysis, followed by the creation of a Flask API to interact with the climate data.

Project Structure
The project is divided into two main parts:

Data Analysis and Exploration:

Analyzing precipitation data for the last 12 months.
Identifying the most active weather stations.
Calculating summary statistics for temperature observations.
Flask API Development:

Creating a Flask application to serve climate data via different API routes.
Developing dynamic routes to calculate temperature statistics for a given start or start-end date range.
Requirements
Python 3.x
SQLAlchemy
Pandas
Matplotlib
Flask
Jupyter Notebook
Setup and Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/Dozsoybootcamp/sqlalchemy-challenge.git
Navigate to the Project Directory:

bash
Copy code
cd sqlalchemy-challenge
Install the Required Packages:

Copy code
pip install -r requirements.txt
Run the Jupyter Notebook:
Open the climate_starter.ipynb in Jupyter Notebook and run the cells to perform the analysis.

Run the Flask Application:

Copy code
python app.py
Jupyter Notebook Analysis
Database Connection
The project connects to the hawaii.sqlite database using SQLAlchemy's create_engine function.
The database schema is reflected using the automap_base function, and the measurement and station tables are mapped to Python classes.
Precipitation Analysis
The analysis begins by identifying the most recent date in the dataset.
A query is performed to retrieve the last 12 months of precipitation data, which is then stored in a Pandas DataFrame.
The data is sorted by date and plotted to visualize the precipitation trends.
Summary statistics for the precipitation data are calculated using Pandas.
Station Analysis
A query is designed to calculate the total number of stations in the dataset.
The most active station is identified based on the number of observations.
A query is performed to retrieve temperature observations for the last 12 months for the most active station, and the results are plotted as a histogram.
Closing the Session
The session is closed at the end of the notebook to ensure proper resource management.
Flask API Development
Available Routes
/: Lists all available API routes.
/api/v1.0/precipitation: Returns the last 12 months of precipitation data as JSON.
/api/v1.0/stations: Returns a JSON list of all weather stations.
/api/v1.0/tobs: Returns temperature observations for the most active station for the last 12 months.
/api/v1.0/<start>: Returns the minimum, average, and maximum temperature for all dates greater than or equal to the start date.
/api/v1.0/<start>/<end>: Returns the minimum, average, and maximum temperature for dates between the start and end date.
Deployment
This project is deployed locally. To run the application:

Start the Flask server by running python app.py.
Access the API endpoints via http://localhost:5000/.

