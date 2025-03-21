from typing import Any, List


def main(values: List[Any]) -> List[Any]:
    swapped = True
    while swapped:
        swapped = False
        for index_a in range(len(values) - 1):
            index_b = index_a + 1
            if values[index_a] > values[index_b]:
                values[index_a], values[index_b] = values[index_b], values[index_a]
                swapped = True

    return values
