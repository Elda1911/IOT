# IoT Edge Temperature Sensor Simulation

A simple Python script that simulates an IoT temperature sensor and demonstrates **Edge Computing** concepts by performing local threshold-based decision-making.

## What it does
- Simulates a temperature sensor generating random readings between 20°C and 32°C.
- Applies edge-level logic: if the temperature exceeds 28°C, it triggers a local alert.
- Runs 5 iterations with a 1-second interval between readings.

## Why this matters
This prototype demonstrates the core idea of **Edge Computing**: processing data and making decisions locally, rather than sending all data to the cloud.

## Tech Stack
- Python 3
- Standard libraries: `random`, `time`
