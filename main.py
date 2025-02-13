from geopy.geocoders import Nominatim

# Function to get geographic coordinates of a location
def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="geo_finder")
    location = geolocator.geocode(location_name)
    
    if location:
        return location.latitude, location.longitude
    else:
        return None

# Function to save coordinates to a file
def save_coordinates(location_name, coordinates):
    with open("coordinates.txt", "a") as file:
        file.write(f"{location_name}: {coordinates}\n")

def main():
    print("Welcome to the Geographic Coordinate Finder!")
    location_name = input("Enter a location: ")
    
    coordinates = get_coordinates(location_name)
    
    if coordinates:
        print(f"The coordinates for {location_name} are {coordinates}")
        save_coordinates(location_name, coordinates)
    else:
        print(f"Could not find coordinates for {location_name}")

if __name__ == "__main__":
    main()
