# Smart Election Lights 2024

This Python script scrapes electoral vote predictions from 270towin.com and controls Sengled smart lights to display red for a Republican victory or blue for a Democratic victory when either candidate reaches 270 electoral votes.

## Requirements

- Python 3.x
- Sengled Smart Lights
- Chrome/Chromium browser (for Selenium)

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Sengled credentials:
```
SENGLED_USERNAME=your_username
SENGLED_PASSWORD=your_password
```

## Usage

Run the script normally to continuously monitor electoral votes:
```bash
python smart-election-2024.py
```

### Testing

The script includes test modes to simulate both Democratic and Republican victories:

```bash
# Test Democratic victory scenario (sets lights to blue)
python smart-election-2024.py --test-dem

# Test Republican victory scenario (sets lights to red)
python smart-election-2024.py --test-rep
```

### Demo Videos

You can find demonstration videos of both scenarios embedded below:

- Democratic victory scenario (lights changing to blue):

<video width="640" height="360" controls>
  <source src="assets/test-dem.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

- Republican victory scenario (lights changing to red):

<video width="640" height="360" controls>
  <source src="assets/test-rep.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Features

- Real-time electoral vote monitoring from 270towin.com
- Automatic light color changes based on electoral results
- Test modes for simulating both victory scenarios
- Detailed logging
- Configurable through environment variables

## Notes

- The script checks for updates every 30 seconds when not in test mode
- Requires Chrome/Chromium browser for web scraping
- All Sengled lights connected to the account will change color
