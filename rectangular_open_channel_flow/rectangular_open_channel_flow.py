import streamlit as st
import math
import matplotlib.pyplot as plt
from tabulate import tabulate 

st.title('Rectangular Open Channel Flow 🌊')

st.markdown("""
This app calculates the capacity and depth of flow in a rectangular open channel using Manning's equation.
The default n value is 0.013, which is the value for concrete channels.
""")

def flow_depth(b=3.0, z = 2, slope = 0.03, Q_design = 10, dy=0.01, n = 0.013):
    # Constants
    n = 0.013    # Manning's roughness coefficient
    g = 9.81     # Acceleration due to gravity (m/s^2)

    # Convert slope from m(vert)/m(horiz) to slope angle in radians
    s = math.atan(slope)

    # Initialize variables
    y = 0    # Initial flow depth (m)
    Q = 0    # Initial flow rate (m^3/s)
    depth_flow = []    # List to store depth and flow rate at each increment

    # Increment flow depth in dy increments until design flow is reached
    while Q < Q_design and y <= 1.5:
        # Calculate the flow area
        A = b * y

        # Calculate the wetted perimeter
        P = b + 2 * y

        # Calculate the hydraulic radius
        Rh = A / P

        # Calculate the flow rate using Manning's equation
        Q = (1/n) * A * Rh**(2/3) * s**(1/2)

        # Append the depth and flow rate to the list
        depth_flow.append((y, Q))

        # Increase the flow depth by dy
        y += dy

    # Calculate velocity and Froude number at the design flow depth
    A_design = b * depth_flow[-1][0]
    v_design = Q_design / A_design
    Fr_design = v_design / (g * depth_flow[-1][0])**0.5

    # Print results in a table
    table = [
        ['Channel width', f'{b:.3f}', 'm'],
        ['Slope', f'{slope:.3f}', '-'],
        ['Design flow rate', f'{Q_design:.3f}', 'm^3/s'],
        ['Manning\'s roughness coefficient', f'{n:.4f}', '-'],
        ['Output', 'Value', 'Units'],
        ['Design flow depth', f'{depth_flow[-1][0]:.3f}', 'm'],
        ['Design flow area', f'{A_design:.3f}', 'm^2'],
        ['Design wetted perimeter', f'{depth_flow[-1][0]*2+b:.3f}', 'm'],
        ['Design hydraulic radius', f'{A_design/(depth_flow[-1][0]*2+b):.3f}', 'm'],
        ['Actual flow rate', f'{depth_flow[-1][1]:.3f}', 'm^3/s'],
        ['Velocity at design flow depth', f'{v_design:.3f}', 'm/s'],
        ['Froude number at design flow depth', f'{Fr_design:.3f}', '-']
    ]
    #st.markdown(tabulate(table, headers=['', 'Value', 'Units'], tablefmt='pipe'))

    return y, A, P, Rh, Q, v_design, Fr_design, depth_flow

# Create user inputs for channel width, side slope, slope, and design flow rate, and optional dy value
b = st.number_input('Enter the channel bottom width in meters:', min_value=0.01)
n = st.number_input(
    'Enter the Manning\'s roughness coefficient (optional, default is 0.013):',
    min_value=0.0001,
    value=0.013,
    format="%.3f"
)
slope = st.number_input('Enter the slope of the channel (m/m):', min_value=0.01)
Q_design = st.number_input('Enter the design flow rate (m^3/s):', min_value=0.01)
dy = st.number_input('Enter the increment for flow depth (optional, default is 0.01m):', min_value=0.001, value=0.01)

# Execute function and capture results
y, A, P, Rh, Q, v_design, Fr_design ,depth_flow = flow_depth(b, slope, Q_design, dy)

# Print results
st.markdown(f'**Channel Bottom Width:** {b:.3f} m')
st.markdown(f'**Slope:** {slope*100:.0f} %')
st.markdown(f'**Design Flow Rate:** {Q_design:.3f} m³/s')
st.markdown(f'**Manning\'s Roughness Coefficient:** {n:.3f}')
st.markdown(f'**Flow Depth:** {y:.3f} m')
st.markdown(f'**Flow Area:** {A:.3f} m²')
st.markdown(f'**Wetted Perimeter:** {P:.3f} m')
st.markdown(f'**Hydraulic Radius:** {Rh:.3f} m')
st.markdown(f'**Flow Rate:** {Q:.3f} m³/s')
st.markdown(f'**Velocity:** {v_design:.3f} m/s')
st.markdown(f'**Froude Number:** {Fr_design:.3f}')

# Plot results
fig, ax = plt.subplots()
ax.plot([i[0] for i in depth_flow], [i[1] for i in depth_flow])
ax.set_xlabel('Depth (m)')
ax.set_ylabel('Flow rate (m^3/s)')
ax.set_title('Depth/Flow Curve')
ax.annotate(f'Channel Bottom Width = {b:.2f} H:V\nSlope = {slope*100:.0f} %', 
            xy=(0.05, 0.95), 
            xycoords='axes fraction', 
            fontsize=10, 
            ha='left', 
            va='top')

st.pyplot(fig)
