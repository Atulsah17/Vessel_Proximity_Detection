import pandas as pd
import numpy as np
from haversine import haversine
from collections import defaultdict

# Load the data
df = pd.read_csv('sample_data.csv')

# Haversine function (vectorized)
def calculate_distance(lat1, lon1, lat2, lon2):
    return haversine((lat1, lon1), (lat2, lon2))

# Function to find vessel proximity
def find_proximity(df, threshold_distance):
    proximity_events = []

    # Iterate over each timestamp
    for timestamp, group in df.groupby('timestamp'):
        vessels = group.to_dict(orient='records')

        for i, vessel1 in enumerate(vessels):
            for vessel2 in vessels[i+1:]:
                distance = calculate_distance(vessel1['lat'], vessel1['lon'],
                                              vessel2['lat'], vessel2['lon'])
                if distance <= threshold_distance:
                    proximity_events.append({
                        'mmsi': vessel1['mmsi'],
                        'vessel_proximity': vessel2['mmsi'],
                        'timestamp': timestamp
                    })
                    proximity_events.append({
                        'mmsi': vessel2['mmsi'],
                        'vessel_proximity': vessel1['mmsi'],
                        'timestamp': timestamp
                    })

    # Convert to DataFrame
    proximity_df = pd.DataFrame(proximity_events)
    # Group by 'mmsi' and 'timestamp', and aggregate 'vessel_proximity' as a list
    proximity_df = proximity_df.groupby(['mmsi', 'timestamp'])['vessel_proximity'].apply(list).reset_index()

    return proximity_df

# Call the function with the DataFrame and a threshold distance (e.g., 0.5 km)
threshold_distance = 0.5  # kilometers
proximity_df = find_proximity(df, threshold_distance)

# Save or visualize the results
proximity_df.to_csv('vessel_proximity_events.csv', index=False)
