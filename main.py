import requests

def check_driver_updates(driver_url):
    response = requests.get(driver_url)
    driver_info = response.json()

    # Extract driver version and release date
    latest_version = driver_info['version']
    release_date = driver_info['release_date']

    # Compare with the current installed driver version
    current_version = '1.0'  # Replace with your current driver version
    if latest_version > current_version:
        print("New driver update available!")
        print(f"Latest Version: {latest_version}")
        print(f"Release Date: {release_date}")
    else:
        print("Your driver is up to date.")

# Provide the URL to fetch the latest driver information
driver_url = "https://example.com/api/driver-info"

# Check for driver updates
check_driver_updates(driver_url)
