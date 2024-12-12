import streamlit as st

# Function to calculate the number of years to retirement
def calculate_years_to_retirement(
    initial_savings,
    monthly_saving,
    savings_growth_rate,
    investment_growth_rate,
    initial_monthly_spending,
    spending_growth_rate,
    retirement_duration,
):
    current_savings = initial_savings
    annual_savings = monthly_saving * 12
    years = 0

    def annual_spending(years_retired):
        return initial_monthly_spending * 12 * (1 + spending_growth_rate) ** years_retired

    while True:
        # Add annual savings to current savings
        current_savings += annual_savings

        # Apply investment growth
        current_savings *= (1 + investment_growth_rate)

        # Check if the current savings can sustain retirement for the required duration
        remaining_savings = current_savings
        years_retired = 0
        while remaining_savings > 0:
            remaining_savings -= annual_spending(years_retired)
            if remaining_savings < 0:
                break
            years_retired += 1

        if years_retired >= retirement_duration:
            break

        # Update annual savings and years
        annual_savings *= (1 + savings_growth_rate)
        years += 1

    return years

# Streamlit interface
st.title("Retirement Calculator")

st.sidebar.header("Input Parameters")
initial_savings = st.sidebar.number_input("Initial Savings (€)", min_value=0, value=100000)
monthly_saving = st.sidebar.number_input("Monthly Saving (€)", min_value=0, value=3500)
savings_growth_rate = st.sidebar.slider("Savings Growth Rate (%)", 0.0, 10.0, 5.0) / 100
investment_growth_rate = st.sidebar.slider("Investment Growth Rate (%)", 0.0, 10.0, 5.0) / 100
initial_monthly_spending = st.sidebar.number_input("Initial Monthly Spending (€)", min_value=0, value=2000)
spending_growth_rate = st.sidebar.slider("Spending Growth Rate (%)", 0.0, 10.0, 2.0) / 100
retirement_duration = st.sidebar.number_input("Retirement Duration (Years)", min_value=1, value=40)

if st.button("Calculate"):
    years_to_retirement = calculate_years_to_retirement(
        initial_savings,
        monthly_saving,
        savings_growth_rate,
        investment_growth_rate,
        initial_monthly_spending,
        spending_growth_rate,
        retirement_duration,
    )
    st.success(f"You need to save for approximately {years_to_retirement} years.")
