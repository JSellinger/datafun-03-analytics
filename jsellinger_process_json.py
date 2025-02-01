"""
Process a JSON file to count astronauts by spacecraft and save the result.

JSON file is in the format where people is a list of dictionaries with keys "craft" and "name".

{
    "people": [
        {
            "craft": "ISS",
            "name": "Oleg Kononenko"
        },
        {
            "craft": "ISS",
            "name": "Nikolai Chub"
        }
    ],
    "number": 2,
    "message": "success"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def iss_position(file_path: pathlib.Path) -> dict:
    """Retrieve iss position from a JSON file."""
    try:
        with file_path.open('r') as file:
            # Use the json module load() function 
            # to read data file into a Python dictionary
            iss_position_dictionary = json.load(file)  
            # initialize an empty dictionary to store the counts
            iss_position =  iss_position_dictionary.get("iss_position")
            if iss_position: # Check if iss_position exists
                latitude = iss_position.get("latitude")
                longitude = iss_position.get("longitude")
                if latitude is not None and longitude is not None: #Check if latitude and longitude are present
                  return {"latitude": latitude, "longitude": longitude}
                else:
                  logger.warning(f"Latitude or Longitude missing from the iss_position data: {iss_position}")
                  return {} # Return empty if lat/long are not present

            else:
                logger.warning("iss_position data not found in the JSON.")
                return {}  # Return an empty dictionary if iss_position is missing

    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, extract ISS position, and save the result."""
    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, "iss-now.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, "iss_location.txt")

    iss_location = iss_position(input_file)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open('w') as file:
        if iss_location:
            file.write(f"ISS Latitude: {iss_location['latitude']}\n")
            file.write(f"ISS Longitude: {iss_location['longitude']}\n")
        else:
            file.write("ISS location data not found.\n")

    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")


if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")