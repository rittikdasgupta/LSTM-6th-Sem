from typing import List, Dict

def transformer(temperature_data: Dict[str, List]) -> List:

    temperature_list = []

    for i in temperature_data["temperatures"]:
        temperature_list.append(i["temperature_in_celsius"])

    return temperature_list

