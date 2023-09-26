import os
import pandas as pd
import subprocess

my_string = "https://www.circl.lu/opendata/datasets/circl-phishing-dataset-01/Clean_phishing/"
custom_url = []
# Open the file for reading
with open("/Users/kayle/Projects/Python/helloworld/temp2", "r") as file:
    # Loop through the contents of the file line by line
    for line in file:
        # Append each line to the string variable with a newline character
        custom_url.append(my_string +line)

# Print the final string
print(custom_url[:5])

df = pd.DataFrame({"URL":custom_url})
df.to_csv('urls.csv', index = False)

print(df.head())

'''
# Directory to save downloaded images
download_directory = "downloaded_images"

# Create the download directory if it doesn't exist
os.makedirs(download_directory, exist_ok=True)

#
# Loop through the image URLs and use wget to download them
for url in custom_url:
    try:
        # Extract the filename from the URL
        filename = os.path.join(download_directory, os.path.basename(url))

        # Use subprocess to run wget to download the image
        subprocess.run(["wget", url, "-O", filename])

        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# List the downloaded images in the download directory
downloaded_images = os.listdir(download_directory)
print("\nDownloaded Images:")
for image in downloaded_images:
    print(os.path.join(download_directory, image))
'''