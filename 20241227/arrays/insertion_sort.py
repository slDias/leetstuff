from typing import List, Any


def main(values: List[Any]) -> List[Any]:
    for lead_index in range(len(values)):
        current_index = lead_index
        left_index = lead_index - 1
        while left_index >= 0 and values[left_index] > values[current_index]:
            values[current_index], values[left_index] = values[left_index], values[current_index]
            left_index -= 1
            current_index -= 1

    return values
