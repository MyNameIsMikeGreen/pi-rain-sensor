Pi Rain Sensor
==============

# Overview

Detects rain using a sensor which sets a pin to high when dry and low when wet.

Polls sensor every few seconds. Sounds buzzer if rain detected. Activity suspended for some amount of time after buzzer last sounded.

All timings are configurable using constants.

# Usage

Configure constants in `main.py` to set appropriate GPIO pins and desired timings. Then execute:

```
python3 main.py
```
