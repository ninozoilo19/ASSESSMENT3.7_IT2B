def build_unique_letter_array(full_name: str) -> list[str]:

    seen = set()
    unique_letters = []

    for ch in full_name.upper():

        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            unique_letters.append(ch)

    return unique_letters


def insertion_sort(arr: list[str]) -> list[str]:

    sorted_arr = arr.copy()

    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
    return sorted_arr


if __name__ == "__main__":
    full_name = "NIÑO CRIS ZOILO"
    unsorted_array = build_unique_letter_array(full_name)
    sorted_array = insertion_sort(unsorted_array)

    print("Unsorted Array:", unsorted_array)
    print("Sorted Array  :", sorted_array)