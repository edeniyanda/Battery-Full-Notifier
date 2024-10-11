# Battery-Full-Notifier

A Python script that notifies users when their device battery is fully charged, promoting energy-efficient usage. It runs in the background, delivering prompt desktop notifications for hassle-free power management.

## Features

- Notifies you when your battery is fully charged.
- Runs in the background with minimal resource usage.
- Plays a sound to alert the user when charging is complete.

## Prerequisites

Ensure you have the following installed on your machine:

1. Python 3.x: Make sure you have Python 3.x installed. You can download it from https://www.python.org/downloads/.
2. pip: Python package manager (pip) should be installed to handle dependencies.

## Installation

1. Clone the repository:  
   Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/yourusername/Battery-Full-Notifier.git
    ```

2. Navigate to the project directory:  
   Change to the directory where the repository was cloned:
   ```bash
   cd Battery-Full-Notifier
   ```

3. Install the required dependencies:  
   Install the necessary Python packages listed in the requirements.txt file:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Script

1. Start the Python Script:  
   Run the main script that monitors the battery and gives a notification when it's fully charged:
   ```python 
    main.py
    ```

2. Battery Charged Notification:  
   When your device battery reaches 100%, the script will:
   - Play a notification sound (stored in battery_charged.mp3).
   - Display a desktop notification.

3. Prevent Sudden Loud Noise:  
   In recent updates, a feature was added to prevent sudden loud noise when a media file is being played.

## Troubleshooting

If you encounter issues with the notification or the sound not playing:

- Ensure that your system notifications are enabled.
- Check if the sound file (battery_charged.mp3) exists in the same directory as main.py.
- Verify that your system volume is turned up and not muted.

## Contributing

If you would like to contribute to the project, feel free to fork the repository and submit a pull request.
