# Vessel_Proximity_Detection
This repository contains the code and documentation for detecting vessel proximity events using latitude, longitude, and timestamp data. The project uses the Haversine formula to calculate distances between vessels and identifies when two vessels come within a threshold distance of each other.

Table of Contents
Project Overview
Installation
Usage
Algorithm Details
Data
Output
Contributing
License
Project Overview
Marine vessels are tracked using their Maritime Mobile Service Identity (MMSI), a unique 9-digit number. The goal of this project is to identify instances where two vessels, with different MMSIs, come within a specified threshold distance during a given timeframe.

Installation
To run this project, you need Python installed on your system along with the following Python libraries:

pandas
numpy
geopy
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Usage
To run the vessel proximity detection algorithm, follow these steps:


Run the script:

bash
Copy code
python main.py
The output will be saved in a file named vessel_proximity_events.csv.

Algorithm Details
The algorithm operates as follows:

Data Processing: The input data is read from a CSV file containing the positions (latitude, longitude) and timestamps of vessels identified by their MMSI.

Distance Calculation: The Haversine formula is used to calculate the great-circle distance between two points on the Earth's surface. This formula is applied to all pairs of vessels within the same timeframe to determine if they are within the threshold distance.

Proximity Detection: The algorithm identifies and records instances where two vessels come within the specified distance. The results are grouped by timestamp.

Output: The output is a CSV file containing the following columns:

mmsi: The unique identifier of a vessel.
timestamp: The time at which the proximity event occurred.
vessel_proximity: A list of MMSIs that came within the threshold distance of the given vessel.
Data
The dataset should be in CSV format with the following columns:

mmsi: int
lat: float (latitude)
lon: float (longitude)
timestamp: datetime (timestamp of the position)
Output
The output file vessel_proximity_events.csv contains the proximity events for each vessel in the dataset.

Sample output:

less
Copy code
mmsi,timestamp,vessel_proximity
218719092,2023-03-14 18:30:00+00,[232345740]
218719092,2023-03-15 01:30:00+00,"[875832716, 232006548, 889799564, 232345740]"
...
