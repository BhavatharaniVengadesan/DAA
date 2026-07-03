import streamlit as st
import time

# ---------------- Interpolation Search ----------------
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        if arr[high] == arr[low]:
            break

        pos = low + int(((target - arr[low]) * (high - low)) /
                        (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


# ---------------- Binary Search ----------------
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# ---------------- UI ----------------
st.title("Interpolation Search vs Binary Search")

st.write("Enter sorted numbers separated by commas.")

numbers = st.text_input(
    "Array",
    "2,5,10,15,23,35,48,60,75,90,105,120"
)

target = st.number_input("Target", value=35)

if st.button("Search"):

    try:
        arr = list(map(int, numbers.split(",")))
        arr.sort()

        # Interpolation Search
        start = time.perf_counter()
        idx1, comp1 = interpolation_search(arr, target)
        time1 = (time.perf_counter() - start) * 1000

        # Binary Search
        start = time.perf_counter()
        idx2, comp2 = binary_search(arr, target)
        time2 = (time.perf_counter() - start) * 1000

        st.subheader("Results")

        col1, col2 = st.columns(2)

        with col1:
            st.success("Interpolation Search")
            st.write("Index :", idx1)
            st.write("Comparisons :", comp1)
            st.write(f"Time : {time1:.6f} ms")

        with col2:
            st.info("Binary Search")
            st.write("Index :", idx2)
            st.write("Comparisons :", comp2)
            st.write(f"Time : {time2:.6f} ms")

    except:
        st.error("Please enter valid integers separated by commas.")