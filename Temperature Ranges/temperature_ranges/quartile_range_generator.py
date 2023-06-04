import numpy as np
from typing import List, Dict

def quartile(temperature_data: List[int]) -> Dict[str, List[float]]:
    
    print("\n\nUnsorted temperature data:", temperature_data)
    # Sorting list for calculating quartile
    temperature_data.sort()

    print(f"\n\nSorted temperature data: {temperature_data}\n\n")

    size_td = len(temperature_data)

    # Calculating quartile points
    q1 = np.quantile(temperature_data, .25, interpolation='midpoint')
    q3 = np.quantile(temperature_data, .75, interpolation='midpoint')

    quartile = {}

    # Generating quartile range output
    quartile["low_range"] = [temperature_data[0],q1]
    quartile["mid_range"] = [q1, q3]
    quartile["high_range"] = [q3, temperature_data[size_td - 1]]

    return quartile