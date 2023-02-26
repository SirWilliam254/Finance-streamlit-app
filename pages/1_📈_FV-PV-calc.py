import streamlit as st
import numpy as np

def calculate_future_value(principal, interest_rate, periods):
    return principal * (1 + interest_rate) ** periods

def calculate_present_value(future_value, interest_rate, periods):
    return future_value / (1 + interest_rate) ** periods

def calculate_interest_rate(future_value, present_value, periods):
    return (future_value / present_value) ** (1 / periods) - 1

def calculate_periods(future_value, present_value, interest_rate):
    return np.log(future_value / present_value) / np.log(1 + interest_rate)

def main():
    st.title("FV,PV,r and n Calculator")

    option = st.selectbox(
        "Select an option",
        ("Calculate Future Value", "Calculate Present Value", "Calculate Interest Rate", "Calculate Number of Periods")
    )

    if option == "Calculate Future Value":
        principal = st.number_input("Enter the principal amount:")
        interest_rate = st.number_input("Enter the interest rate (%):")
        periods = st.number_input("Enter the number of periods:")
        if st.button("calculate"):
            future_value = calculate_future_value(principal, interest_rate / 100, periods)
            st.write("The future value is:", round(future_value, 2))

    elif option == "Calculate Present Value":
        future_value = st.number_input("Enter the future value:")
        interest_rate = st.number_input("Enter the interest rate (%):")
        periods = st.number_input("Enter the number of periods:")
        if st.button("calculate"):
            present_value = calculate_present_value(future_value, interest_rate / 100, periods)
            st.write("The present value is:", round(present_value, 2))

    elif option == "Calculate Interest Rate":
        future_value = st.number_input("Enter the future value:")
        present_value = st.number_input("Enter the present value:")
        periods = st.number_input("Enter the number of periods:")
        if st.button("calculate"):
            interest_rate = calculate_interest_rate(future_value, present_value, periods)
            st.write("The interest rate is:", round(interest_rate * 100, 2), "%")

    elif option == "Calculate Number of Periods":
        future_value = st.number_input("Enter the future value:")
        present_value = st.number_input("Enter the present value:")
        interest_rate = st.number_input("Enter the interest rate (%):")
        if st.button("calculate"):
            periods = calculate_periods(future_value, present_value, interest_rate / 100)
            st.write("The number of periods is:", round(periods, 2))

if __name__ == "__main__":
    main()
