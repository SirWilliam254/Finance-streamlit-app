import streamlit as st
import math

def calculate_simple_interest(principal, rate, time):
    return principal * rate * time

def calculate_compound_interest(principal, rate, time, frequency):
    n = frequency
    return principal * math.pow(1 + (rate / n), n * time)

def calculate_amortized_interest(principal, rate, time, frequency):
    n = frequency
    c = principal * (rate / n) * math.pow(1 + (rate / n), n * time) / (math.pow(1 + (rate / n), n * time) - 1)
    return c * time * n - principal

def calculate_fixed_interest(principal, rate, time):
    return principal * rate * time

def calculate_floating_interest(principal, rate, time, frequency):
    n = frequency
    return principal * math.pow(1 + rate, time)

def calculate_discounted_interest(principal, rate, time, discount_rate):
    return principal * (1 - math.pow(1 - discount_rate, time)) / discount_rate

def calculate_nominal_interest(effective_rate, frequency):
    return effective_rate * frequency

def calculate_real_interest(nominal_rate, inflation_rate):
    return (1 + nominal_rate) / (1 + inflation_rate) - 1

def main():
    st.title("Interest Calculator")

    interest_types = ["Simple Interest", "Compound Interest", "Amortized Interest", "Fixed Interest",
                      "Floating Interest", "Discounted Interest", "Nominal Interest", "Real Interest"]
    option = st.selectbox("Select an interest type", interest_types)

    if option == "Simple Interest":
        principal = st.number_input("Enter the principal amount:")
        rate = st.number_input("Enter the interest rate (%):")
        time = st.number_input("Enter the time period (in years):")
        if st.button("calculate"):
            simple_interest = calculate_simple_interest(principal, rate / 100, time)
            st.write("The simple interest is:", round(simple_interest, 2))

    elif option == "Compound Interest":
        principal = st.number_input("Enter the principal amount:")
        rate = st.number_input("Enter the interest rate (%):")
        time = st.number_input("Enter the time period (in years):")
        frequency = st.number_input("Enter the compounding frequency (per year):")
        if st.button("calculate"):
            compound_interest = calculate_compound_interest(principal, rate / 100, time, frequency)
            st.write("The compound interest is:", round(compound_interest, 2))

    elif option == "Amortized Interest":
        principal = st.number_input("Enter the principal amount:")
        rate = st.number_input("Enter the interest rate (%):")
        time = st.number_input("Enter the time period (in years):")
        frequency = st.number_input("Enter the payment frequency (per year):")
        if st.button("calculate"):
            amortized_interest = calculate_amortized_interest(principal, rate / 100, time, frequency)
            st.write("The amortized interest is:", round(amortized_interest, 2))

    elif option == "Fixed Interest":
        principal = st.number_input("Enter the principal amount:")
        rate = st.number_input("Enter the interest rate (%):")
        time = st.number_input("Enter the time period (in years):")
        if st.button("calculate"):
            fixed_interest = calculate_fixed_interest(principal, rate / 100, time)
            st.write("The fixed interest is:", round(fixed_interest, 2))

    elif option == "Floating Interest":
        principal = st.number_input("Enter the principal amount:")
        rate = st.number_input("Enter the interest rate (%):")
        time = st.number_input("Enter the time period (in years):")
        frequency = st.number_input("Enter the interest rate frequency (per year):")
        if st.button("calculate"):
            floating_interest = calculate_floating_interest(principal, rate / 100, time, frequency)
            st.write("The floating interest is:", round(floating_interest, 2))

    elif option == "Discounted Interest":
        principal = st.number_input("Enter the principal amount:")
        rate = st.number_input("Enter the interest rate (%):")
        time = st.number_input("Enter the time period (in years):")
        discount_rate = st.number_input("Enter the discount rate (%):")
        discounted_interest = calculate_discounted_interest(principal, rate / 100, time, discount_rate / 100)
        st.write("The discounted interest is:", round(discounted_interest, 2))

    elif option == "Nominal Interest":
        effective_rate = st.number_input("Enter the effective interest rate (%):")
        frequency = st.number_input("Enter the compounding frequency (per year):")
        if st.button("calculate"):
            nominal_rate = calculate_nominal_interest(effective_rate / 100, frequency)
            st.write("The nominal interest rate is:", round(nominal_rate * 100, 2), "%")

    elif option == "Real Interest":
        nominal_rate = st.number_input("Enter the nominal interest rate (%):")
        inflation_rate = st.number_input("Enter the inflation rate (%):")
        if st.button("calculate"):
            real_interest = calculate_real_interest(nominal_rate / 100, inflation_rate / 100)
            st.write("The real interest rate is:", round(real_interest * 100, 2), "%")
if __name__ == "__main__":
    main()
