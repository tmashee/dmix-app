
import pyautogui
import pandas as pd
import time
import glob

try:
    # Load the CSV file
    csv_files = glob.glob('*.csv')

    # Check if any CSV files are found
    if csv_files:
        # Read the first CSV file found
        df = pd.read_csv(csv_files[0])
        
        # Concatenate the Spotify URL with Track ID
        df['url'] = 'https://open.spotify.com/track/' + df['Track ID']
        track_ids = df['url']
        
        # Open the Deemx app on Mac using Spotlight
        pyautogui.keyDown('command')
        pyautogui.press('space')
        pyautogui.keyUp('command')
        pyautogui.write('deemix-gui.app')
        pyautogui.press('enter')
        
        # Wait for the app to open
        time.sleep(2)

        # Maximize app window
        pyautogui.hotkey('fn', 'control', 'f')
        time.sleep(2)

        # Click on the search field
        pyautogui.click(x=500, y=70)

        # Initialize counter
        iteration_count = 0

        # Iterate through each url
        for track_id in df['url']:
            # Copy the track ID
            with pyautogui.hold('command'):
                pyautogui.press('a')
            pyautogui.write(str(track_id))
            pyautogui.press('enter')
            time.sleep(1)  # Adjust the sleep time as needed
            
            # Increment counter
            iteration_count += 1

        print(f"{iteration_count} track IDs have been processed.")
    else:
        print("No CSV files found.")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except pd.errors.EmptyDataError as e:
    print(f"Empty data error: {e}")
except pyautogui.FailSafeException as e:
    print(f"PyAutoGUI fail-safe triggered: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
