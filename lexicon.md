
**Injection type**: analog (1) is a physical injection to test the whole system. digital (2) injects further down the line and is therefore better suited to test the program logic. No injection (0) is also possible.  
**Latency**: Gap between detecting event and decision to keep it. Must be exact, as the number is an offset in memory.  
**SCurve**: Every single pixel has a s-shaped curve (logistic function) with the threshold in the middle. The width of the curve is determined by noise. The SCurve-graph is the overlay of all single-pixel s-curves.  
**Threshold**: Minimum amplitude a signal needs to be detected. Used to distinguish signal from noise. **TDAC** Value is used to calibrate the thresholds from every single pixel.   **Vthreshold_LIN** is used to calibrate the threshold for every pixel at the same time.  

