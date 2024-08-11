# Import the dependencies.

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# SQLAlchemy imports
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import inspect

# For warnings
import warnings
warnings.filterwarnings('ignore')


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
Base = automap_base()

# Use create_engine to connect to your SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
from flask import Flask, jsonify

# Flask Setup
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query the database for precipitation data
    results = session.query(Measurement.date, Measurement.prcp).all()

    # Convert the query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in results}

    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    # Query the database for stations data
    results = session.query(Station.station).all()

    # Convert the query results to a list
    stations_list = list(np.ravel(results))

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    # Query the dates and temperature observations of the most active station for the last year of data.
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]

    last_year_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]

    year_ago_date = datetime.strptime(last_year_date, '%Y-%m-%d') - timedelta(days=365)

    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= year_ago_date).all()

    tobs_list = list(np.ravel(results))

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all()
    else:
        results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    temp_stats = list(np.ravel(results))

    return jsonify(temp_stats)

if __name__ == '__main__':
    app.run(debug=True)