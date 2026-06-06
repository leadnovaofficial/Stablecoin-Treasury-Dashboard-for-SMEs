import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Stablecoin Treasury Dashboard for SMEs",
    page_icon="💵",
    layout="wide"
)

# App title
st.title("💵 Stablecoin Treasury Dashboard for SMEs")
st.write(
    "A simple treasury dashboard for small businesses holding USDC/USDT "
    "to manage liquidity, upcoming payments, yield opportunities, and FX exposure."
)

st.divider()

# Mock wallet data
wallets = pd.DataFrame({
    "Stablecoin": ["USDC", "USDT"],
    "Total Balance": [30000, 15000],
    "Available Liquidity": [18000, 7000],
    "In Yield": [12000, 8000]
})

# Mock upcoming payables
payables = pd.DataFrame({
    "Vendor": ["Supplier A", "Logistics Partner", "Freelancer B", "Packaging Vendor"],
    "Amount": [8000, 3000, 1200, 2500],
    "Currency": ["USD", "CAD", "USD", "AED"],
    "Due Date": ["2026-06-10", "2026-06-12", "2026-06-08", "2026-06-15"],
    "Status": ["Pending", "Pending", "Urgent", "Pending"]
})

# Mock yield options
yield_options = pd.DataFrame({
    "Yield Option": ["Conservative USDC Pool", "Flexible USDT Pool", "Growth USDC Pool"],
    "Stablecoin": ["USDC", "USDT", "USDC"],
    "Estimated APY": ["4.2%", "5.1%", "7.5%"],
    "Risk Level": ["Low", "Medium", "Medium"],
    "Lock Period": ["Flexible", "7 Days", "30 Days"]
})

# Mock FX exposure
fx_exposure = pd.DataFrame({
    "Currency Needed": ["USD", "CAD", "AED"],
    "Amount Due": [9200, 3000, 2500],
    "Current Treasury Asset": ["USDC/USDT", "USDC", "USDC"],
    "FX Risk Level": ["Low", "Medium", "Medium"]
})

# Calculations
total_balance = wallets["Total Balance"].sum()
available_liquidity = wallets["Available Liquidity"].sum()
funds_in_yield = wallets["In Yield"].sum()
upcoming_payables = payables["Amount"].sum()

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Treasury", f"${total_balance:,.0f}")
col2.metric("Available Liquidity", f"${available_liquidity:,.0f}")
col3.metric("Funds in Yield", f"${funds_in_yield:,.0f}")
col4.metric("Upcoming Payables", f"${upcoming_payables:,.0f}")

st.divider()

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "Payables",
    "Yield Management",
    "FX Exposure",
    "AI Insights"
])

with tab1:
    st.subheader("Stablecoin Wallet Overview")
    st.dataframe(wallets, use_container_width=True)

    st.subheader("Treasury Allocation Chart")
    chart_data = wallets.set_index("Stablecoin")[["Available Liquidity", "In Yield"]]
    st.bar_chart(chart_data)

with tab2:
    st.subheader("Upcoming Payables")
    st.dataframe(payables, use_container_width=True)

    urgent_payments = payables[payables["Status"] == "Urgent"]

    if not urgent_payments.empty:
        st.warning("You have urgent payments due soon. Keep enough liquidity available.")

with tab3:
    st.subheader("Yield Management")
    st.dataframe(yield_options, use_container_width=True)

    st.info(
        "Suggestion: Use flexible yield options when supplier payments are coming soon. "
        "Avoid locking too much stablecoin for long periods."
    )

with tab4:
    st.subheader("FX Exposure")
    st.dataframe(fx_exposure, use_container_width=True)

    st.warning(
        "Some upcoming payments are in non-USD currencies such as CAD and AED. "
        "This creates FX exposure because the business is mainly holding USD stablecoins."
    )

with tab5:
    st.subheader("AI Treasury Insights")

    if available_liquidity >= upcoming_payables:
        st.success(
            "Liquidity looks healthy. You have enough available stablecoins "
            "to cover upcoming payables."
        )
    else:
        st.error(
            "Liquidity risk detected. Upcoming payables are higher than available liquidity."
        )

    idle_amount = available_liquidity - upcoming_payables

    if idle_amount > 0:
        st.info(
            f"You may have around ${idle_amount:,.0f} in excess liquidity "
            "that could be reviewed for yield allocation."
        )
    else:
        st.warning(
            "Do not allocate more funds to yield right now. Keep liquidity available for payments."
        )

    st.write("Additional insights:")
    st.write("- USDC balance is higher than USDT, which may be better for conservative treasury planning.")
    st.write("- CAD and AED payables create FX exposure.")
    st.write("- Flexible yield options are safer when payment dates are near.")
    st.write("- The business should keep enough stablecoin liquid before chasing yield.")
