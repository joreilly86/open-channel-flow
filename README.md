# Rectangular Open Channel Flow Calculator 🌊

## Description
This repository contains a Streamlit app designed to calculate the capacity and depth of flow in a rectangular open channel using Manning's equation.

## Features 🛠️
- Calculation of flow area, wetted perimeter, hydraulic radius, and flow rate.
- Supports user-defined parameters like channel width, slope, Manning's coefficient, and design flow rate.
- Plotting of depth/flow curve for visual inspection.
- Use of tabulate for result presentation.

## Requirements 📦
- Python
- Streamlit
- Matplotlib
- Tabulate

## Installation 🔧
1. Clone this repository.
2. Navigate to the repository directory.
3. Run `pip install -r requirements.txt`.
4. Run `streamlit run <filename.py>` to start the app.

## Usage 🖥️
1. Enter the channel bottom width in meters.
2. Specify the slope of the channel (m/m).
3. (Optional) Provide the Manning's roughness coefficient (default is 0.013).
4. Input the design flow rate (m³/s).
5. (Optional) Specify the increment for flow depth (default is 0.01m).

## Results 📊
The app provides:
- Channel Bottom Width (m)
- Slope (%)
- Design Flow Rate (m³/s)
- Manning's Roughness Coefficient
- Flow Depth (m)
- Flow Area (m²)
- Wetted Perimeter (m)
- Hydraulic Radius (m)
- Flow Rate (m³/s)
- Velocity (m/s)
- Froude Number

## Contributing 🤝
For contributions, please open an issue first to discuss what you would like to change.

## License 📝
This project is open-source, under the MIT License.

Note: This README assumes a filename.py containing the main code. Modify the filenames and commands as necessary.
