from typing import Any, List


def main(values: List[Any]) -> List[Any]:
    sorted_index = 0

    while sorted_index < len(values):
        min_index = sorted_index
        for index in range(sorted_index + 1, len(values)):
            if values[index] < values[min_index]:
                min_index = index

        values[sorted_index], values[min_index] = values[min_index], values[sorted_index]
        sorted_index += 1

    return values