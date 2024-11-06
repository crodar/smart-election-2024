# Smart Election Lights 2024

This Python script scrapes electoral vote predictions from 270towin.com and controls Sengled smart lights to display red for a Republican victory or blue for a Democratic victory when either candidate reaches 270 electoral votes.


## Demo Videos

- Democratic victory scenario (lights changing to blue):

![test-dem](https://github.com/user-attachments/assets/b7dc43b4-9465-49d9-9832-1e2d5711cc7a)


- Republican victory scenario (lights changing to red):

![test-rep](https://github.com/user-attachments/assets/e1983dac-3994-4c23-b22c-a52656d039c0)


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

3. Rename `.env.template` to `.env` and enter your Sengled credentials:
```bash
mv .env.template .env
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
