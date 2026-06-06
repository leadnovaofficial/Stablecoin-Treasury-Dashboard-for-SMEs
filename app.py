import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Stablecoin Treasury Dashboard for SMEs",
    page_icon="💵",
    layout="wide"
)

# Title
st.title("💵 Stablecoin Treasury Dashboard for SMEs")
st.write(
    "A simple treasury dashboard for small businesses holding USDC/USDT "
    "to manage liquidity, upcoming payments, yield opportunities, and FX exposure."
)

st.divider()

# Sidebar inputs
st.sidebar.header("Treasury Inputs")

usdc_balance = st.sidebar.number_input(
    "USDC Balance",
    min_value=0,
    value=30000,
    step=1000
)

usdt_balance = st.sidebar.number_input(
    "USDT Balance",
    min_value=0,
    value=15000,
    step=1000
)

usdc_in_yield = st.sidebar.number_input(
    "USDC in Yield",
    min_value=0,
    max_value=usdc_balance,
    value=12000,
    step=1000
)

usdt_in_yield = st.sidebar.number_input(
    "USDT in Yield",
    min_value=0,
    max_value=usdt_balance,
    value=8000,
    step=1000
)

st.sidebar.header("FX Rates")

cad_rate = st.sidebar.number_input(
    "1 USD to CAD",
    min_value=0.0,
    value=1.37,
    step=0.01
)

aed_rate = st.sidebar.number_input(
    "1 USD to AED",
    min_value=0.0,
    value=3.67,
    step=0.01
)

# Calculations
usdc_available = usdc_balance - usdc_in_yield
usdt_available = usdt_balance - usdt_in_yield

wallets = pd.DataFrame({
    "Stablecoin": ["USDC", "USDT"],
    "Total Balance": [usdc_balance, usdt_balance],
    "Available Liquidity": [usdc_available, usdt_available],
    "In Yield": [usdc_in_yield, usdt_in_yield]
})

# Editable payables data
default_payables = pd.DataFrame({
    "Vendor": ["Supplier A", "Logistics Partner", "Freelancer B", "Packaging Vendor"],
    "Amount": [8000, 3000, 1200, 2500],
    "Currency": ["USD", "CAD", "USD", "AED"],
    "Due Date": ["2026-06-10", "2026-06-12", "2026-06-08", "2026-06-15"],
    "Status": ["Pending", "Pending", "Urgent", "Pending"]
})

# Yield options
yield_options = pd.DataFrame({
    "Yield Option": ["Conservative USDC Pool", "Flexible USDT Pool", "Growth USDC Pool"],
    "Stablecoin": ["USDC", "USDT", "USDC"],
    "Estimated APY": ["4.2%", "5.1%", "7.5%"],
    "Risk Level": ["Low", "Medium", "Medium"],
    "Lock Period": ["Flexible", "7 Days", "30 Days"]
})

# FX exposure
fx_exposure = pd.DataFrame({
    "Currency Needed": ["USD", "CAD", "AED"],
    "Example Amount Due": [9200, 3000, 2500],
    "Current Treasury Asset": ["USDC/USDT", "USDC", "USDC"],
    "FX Rate Used": ["1.00", cad_rate, aed_rate],
    "FX Risk Level": ["Low", "Medium", "Medium"]
})

# Main dashboard calculations
total_balance = wallets["Total Balance"].sum()
available_liquidity = wallets["Available Liquidity"].sum()
funds_in_yield = wallets["In Yield"].sum()

# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Treasury", f"${total_balance:,.0f}")
col2.metric("Available Liquidity", f"${available_liquidity:,.0f}")
col3.metric("Funds in Yield", f"${funds_in_yield:,.0f}")
col4.metric("Stablecoins Used", "USDC / USDT")

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

    st.info(
        "Use the sidebar inputs to change stablecoin balances and see the dashboard update automatically."
    )

with tab2:
    st.subheader("Upcoming Payables")

    edited_payables = st.data_editor(
        default_payables,
        use_container_width=True,
        num_rows="dynamic"
    )

    upcoming_payables = edited_payables["Amount"].sum()

    st.metric("Total Upcoming Payables", f"${upcoming_payables:,.0f}")

    urgent_payments = edited_payables[edited_payables["Status"] == "Urgent"]

    if not urgent_payments.empty:
        st.warning("You have urgent payments due soon. Keep enough liquidity available.")
    else:
        st.success("No urgent payments found.")

with tab3:
    st.subheader("Yield Management")
    st.dataframe(yield_options, use_container_width=True)

    idle_liquidity = available_liquidity - default_payables["Amount"].sum()

    st.subheader("Yield Recommendation")

    if idle_liquidity > 0:
        st.success(
            f"You may have around ${idle_liquidity:,.0f} in excess liquidity. "
            "This amount can be reviewed for flexible yield allocation."
        )
    else:
        st.warning(
            "You do not have excess liquidity right now. Avoid locking more funds into yield."
        )

    st.info(
        "For SMEs, flexible yield options are safer when supplier payments are coming soon."
    )

with tab4:
    st.subheader("FX Exposure")
    st.dataframe(fx_exposure, use_container_width=True)

    st.write("FX exposure means currency risk when the business holds USD stablecoins but needs to pay in other currencies.")

    cad_example = 3000 / cad_rate
    aed_example = 2500 / aed_rate

    col_fx1, col_fx2 = st.columns(2)

    col_fx1.metric("CAD 3,000 Payment in USD", f"${cad_example:,.2f}")
    col_fx2.metric("AED 2,500 Payment in USD", f"${aed_example:,.2f}")

    st.warning(
        "If exchange rates change, the final payment cost can increase or decrease."
    )

with tab5:
    st.subheader("AI Treasury Insights")

    total_payables = default_payables["Amount"].sum()

    if available_liquidity >= total_payables:
        st.success(
            "Liquidity looks healthy. You have enough available stablecoins "
            "to cover upcoming payables."
        )
    else:
        st.error(
            "Liquidity risk detected. Upcoming payables are higher than available liquidity."
        )

    idle_amount = available_liquidity - total_payables

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
    st.write("- USDC balance is useful for conservative treasury planning.")
    st.write("- CAD and AED payables create FX exposure.")
    st.write("- Flexible yield options are better when payment dates are near.")
    st.write("- The business should keep enough stablecoin liquid before chasing yield.")
