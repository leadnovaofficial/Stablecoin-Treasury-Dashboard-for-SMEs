import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="StableFlow | Stablecoin Treasury OS",
    page_icon="💵",
    layout="wide"
)

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    .big-title {
        font-size: 48px;
        font-weight: 800;
        line-height: 1.1;
    }
    .subtitle {
        font-size: 20px;
        color: #555;
        margin-bottom: 20px;
    }
    .pitch-card {
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #e6e6e6;
        background-color: #fafafa;
        height: 100%;
    }
    .highlight-card {
        padding: 22px;
        border-radius: 16px;
        background-color: #ecfdf3;
        border: 1px solid #abefc6;
        height: 100%;
    }
    .risk-card {
        padding: 22px;
        border-radius: 16px;
        background-color: #fff4e5;
        border: 1px solid #ffd59e;
        height: 100%;
    }
    .danger-card {
        padding: 22px;
        border-radius: 16px;
        background-color: #fff1f3;
        border: 1px solid #fecdd3;
        height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar: Business scenario
# -----------------------------
st.sidebar.title("Scenario Builder")

company_name = st.sidebar.text_input("Business Name", "NorthBridge Imports")
business_type = st.sidebar.selectbox(
    "Business Type",
    ["Importer", "Exporter", "Logistics Company", "Digital Agency", "Marketplace", "Freelance Team"]
)

main_region = st.sidebar.selectbox(
    "Primary Market",
    ["Canada", "UAE", "United States", "United Kingdom", "Pakistan", "Singapore"]
)

monthly_revenue = st.sidebar.number_input(
    "Monthly Revenue",
    min_value=0,
    value=85000,
    step=5000
)

st.sidebar.divider()

st.sidebar.subheader("Stablecoin Treasury")

usdc_balance = st.sidebar.number_input("USDC Balance", min_value=0, value=30000, step=1000)
usdt_balance = st.sidebar.number_input("USDT Balance", min_value=0, value=15000, step=1000)

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

target_yield_apy = st.sidebar.slider(
    "Target Yield APY",
    min_value=0.0,
    max_value=15.0,
    value=5.2,
    step=0.1
)

st.sidebar.divider()

st.sidebar.subheader("FX Rates")

cad_rate = st.sidebar.number_input("1 USD to CAD", min_value=0.01, value=1.37, step=0.01)
aed_rate = st.sidebar.number_input("1 USD to AED", min_value=0.01, value=3.67, step=0.01)
eur_rate = st.sidebar.number_input("1 USD to EUR", min_value=0.01, value=0.92, step=0.01)

st.sidebar.divider()

st.sidebar.subheader("Business Assumptions")

bank_fee_pct = st.sidebar.slider(
    "Current Bank / Transfer Fee %",
    min_value=0.0,
    max_value=5.0,
    value=1.2,
    step=0.1
)

payment_delay_days = st.sidebar.slider(
    "Current Payment Delay in Days",
    min_value=0,
    max_value=10,
    value=3
)

# -----------------------------
# Data
# -----------------------------
usdc_available = usdc_balance - usdc_in_yield
usdt_available = usdt_balance - usdt_in_yield

total_balance = usdc_balance + usdt_balance
funds_in_yield = usdc_in_yield + usdt_in_yield
available_liquidity = usdc_available + usdt_available

wallets = pd.DataFrame({
    "Stablecoin": ["USDC", "USDT"],
    "Total Balance": [usdc_balance, usdt_balance],
    "Available Liquidity": [usdc_available, usdt_available],
    "In Yield": [usdc_in_yield, usdt_in_yield]
})

default_payables = pd.DataFrame({
    "Vendor": ["Supplier A", "Logistics Partner", "Freelancer B", "Packaging Vendor"],
    "Category": ["Inventory", "Shipping", "Services", "Operations"],
    "Amount": [8000, 3000, 1200, 2500],
    "Currency": ["USD", "CAD", "USD", "AED"],
    "Due in Days": [5, 9, 2, 14],
    "Status": ["Pending", "Pending", "Urgent", "Pending"]
})

yield_options = pd.DataFrame({
    "Yield Product": ["Flexible USDC Vault", "Short-Term USDT Pool", "Growth USDC Strategy"],
    "Stablecoin": ["USDC", "USDT", "USDC"],
    "Estimated APY": ["4.2%", "5.1%", "7.5%"],
    "Risk Level": ["Low", "Medium", "Medium"],
    "Lock Period": ["Flexible", "7 Days", "30 Days"],
    "Best For": ["Emergency liquidity", "Short cash parking", "Idle long-term funds"]
})

pricing = pd.DataFrame({
    "Plan": ["Starter", "Growth", "Treasury Pro"],
    "Target Customer": ["Small SME", "Growing importer/exporter", "Multi-currency business"],
    "Monthly Price": ["$49", "$149", "$399"],
    "Key Feature": ["Basic dashboard", "FX + yield insights", "Advanced treasury automation"]
})

# -----------------------------
# Header / Hero
# -----------------------------
st.markdown('<div class="big-title">StableFlow: Stablecoin Treasury OS for SMEs</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Helping small businesses manage stablecoin liquidity, supplier payables, FX exposure, and yield opportunities from one CFO-friendly dashboard.</div>',
    unsafe_allow_html=True
)

col_a, col_b, col_c = st.columns([1.1, 1, 1])

with col_a:
    st.markdown(
        """
        <div class="highlight-card">
        <h3>Business Pitch</h3>
        <p><b>StableFlow</b> is a treasury management platform for SMEs that hold USDC/USDT and need better control over payments, idle cash, currency risk, and yield.</p>
        <p>Think: <b>Brex-style treasury dashboard + stablecoin finance layer</b>.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_b:
    st.markdown(
        """
        <div class="pitch-card">
        <h3>Target Customer</h3>
        <p>Non-crypto-native CFOs, finance managers, importers, exporters, agencies, and small businesses using stablecoins for global payments.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_c:
    st.markdown(
        """
        <div class="risk-card">
        <h3>Core Pain</h3>
        <p>SMEs may hold stablecoins, but they lack one simple tool to manage liquidity, yield, FX exposure, and upcoming payables together.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# -----------------------------
# Editable Payables
# -----------------------------
st.subheader("Interactive Payables Planner")

st.write(
    "Edit the supplier payments below. The dashboard will update the liquidity score, risk level, and business case automatically."
)

edited_payables = st.data_editor(
    default_payables,
    use_container_width=True,
    num_rows="dynamic",
    hide_index=True,
    column_config={
        "Currency": st.column_config.SelectboxColumn(
            "Currency",
            options=["USD", "CAD", "AED", "EUR"]
        ),
        "Status": st.column_config.SelectboxColumn(
            "Status",
            options=["Pending", "Urgent", "Paid"]
        ),
        "Amount": st.column_config.NumberColumn(
            "Amount",
            min_value=0,
            step=100
        ),
        "Due in Days": st.column_config.NumberColumn(
            "Due in Days",
            min_value=0,
            step=1
        )
    }
)

edited_payables["Amount"] = pd.to_numeric(edited_payables["Amount"], errors="coerce").fillna(0)
edited_payables["Due in Days"] = pd.to_numeric(edited_payables["Due in Days"], errors="coerce").fillna(0)
edited_payables["Currency"] = edited_payables["Currency"].fillna("USD")
edited_payables["Status"] = edited_payables["Status"].fillna("Pending")

fx_rates = {
    "USD": 1.00,
    "CAD": cad_rate,
    "AED": aed_rate,
    "EUR": eur_rate
}

def convert_to_usd(row):
    currency = row["Currency"]
    amount = row["Amount"]
    rate = fx_rates.get(currency, 1.00)
    return amount / rate

edited_payables["USD Equivalent"] = edited_payables.apply(convert_to_usd, axis=1)

total_payables_usd = edited_payables["USD Equivalent"].sum()
urgent_payables_usd = edited_payables[
    (edited_payables["Status"] == "Urgent") | (edited_payables["Due in Days"] <= 3)
]["USD Equivalent"].sum()

idle_liquidity = available_liquidity - total_payables_usd
annual_yield_estimate = funds_in_yield * (target_yield_apy / 100)
monthly_yield_estimate = annual_yield_estimate / 12
monthly_fee_savings = total_payables_usd * (bank_fee_pct / 100)
estimated_monthly_value = monthly_yield_estimate + monthly_fee_savings

coverage_ratio = available_liquidity / total_payables_usd if total_payables_usd > 0 else 10

liquidity_score = 50

if coverage_ratio >= 1.5:
    liquidity_score += 25
elif coverage_ratio >= 1.0:
    liquidity_score += 15
elif coverage_ratio >= 0.75:
    liquidity_score += 5
else:
    liquidity_score -= 20

if idle_liquidity > 0:
    liquidity_score += 10
else:
    liquidity_score -= 15

if total_balance > 0 and funds_in_yield <= total_balance * 0.45:
    liquidity_score += 10
else:
    liquidity_score -= 5

if urgent_payables_usd <= available_liquidity * 0.35:
    liquidity_score += 5
else:
    liquidity_score -= 10

liquidity_score = max(0, min(100, liquidity_score))

if liquidity_score >= 80:
    risk_label = "Low Risk"
elif liquidity_score >= 60:
    risk_label = "Medium Risk"
else:
    risk_label = "High Risk"

runway_days = (available_liquidity / total_payables_usd) * 30 if total_payables_usd > 0 else 999

st.divider()

# -----------------------------
# Executive Metrics
# -----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Treasury", f"${total_balance:,.0f}")
col2.metric("Available Liquidity", f"${available_liquidity:,.0f}")
col3.metric("Upcoming Payables", f"${total_payables_usd:,.0f}")
col4.metric("Idle Liquidity", f"${idle_liquidity:,.0f}")
col5.metric("Risk Level", risk_label)

st.progress(liquidity_score / 100)
st.caption(f"Liquidity Score: {liquidity_score}/100 | Estimated runway: {runway_days:.0f} days")

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Pitch Overview",
    "Product Demo",
    "AI CFO Insights",
    "FX + Yield Simulator",
    "Business Model",
    "Final Project Summary"
])

# -----------------------------
# Tab 1: Pitch Overview
# -----------------------------
with tab1:
    st.header("Pitch Overview")

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Problem")
        st.markdown(
            """
            SMEs are starting to use stablecoins for global payments, but their finance teams still manage treasury through spreadsheets, wallets, exchanges, and bank portals.

            This creates four major problems:

            - No clear view of available liquidity
            - No easy planning for supplier payables
            - Idle stablecoins are not optimized for yield
            - FX exposure is hard to understand
            """
        )

    with c2:
        st.subheader("Solution")
        st.markdown(
            """
            StableFlow gives SMEs one dashboard to manage their stablecoin treasury.

            The platform helps CFOs answer:

            - How much stablecoin do we have?
            - How much is liquid today?
            - What payments are due soon?
            - Can we safely allocate idle funds to yield?
            - Which currency exposures create risk?
            """
        )

    st.subheader("Why Now?")
    st.info(
        "Stablecoins are becoming more relevant for global B2B payments, but most SME finance teams are not crypto-native. "
        "They need simple treasury software, not complex DeFi tools."
    )

    st.subheader("One-Line Value Proposition")
    st.success(
        "StableFlow helps SMEs turn stablecoin balances into a controlled treasury system for liquidity, payables, FX, and yield."
    )

# -----------------------------
# Tab 2: Product Demo
# -----------------------------
with tab2:
    st.header("Product Demo")

    st.subheader(f"{company_name} Treasury Snapshot")

    demo_col1, demo_col2 = st.columns(2)

    with demo_col1:
        st.write("Stablecoin Wallets")
        st.dataframe(wallets, use_container_width=True, hide_index=True)

    with demo_col2:
        st.write("Treasury Allocation")
        chart_data = wallets.set_index("Stablecoin")[["Available Liquidity", "In Yield"]]
        st.bar_chart(chart_data)

    st.subheader("Upcoming Payables in USD Equivalent")
    st.dataframe(edited_payables, use_container_width=True, hide_index=True)

    if available_liquidity >= total_payables_usd:
        st.success("The business has enough available stablecoins to cover upcoming payments.")
    else:
        st.error("Liquidity gap detected. Available stablecoins are lower than upcoming payables.")

# -----------------------------
# Tab 3: AI CFO Insights
# -----------------------------
with tab3:
    st.header("AI CFO Insights")

    st.subheader("Executive Memo")

    if risk_label == "Low Risk":
        st.success(
            f"{company_name} has a healthy treasury position. Available liquidity covers upcoming payments, "
            "and the company may review excess liquidity for flexible yield allocation."
        )
    elif risk_label == "Medium Risk":
        st.warning(
            f"{company_name} has manageable liquidity, but treasury decisions should be cautious. "
            "Avoid locking too much stablecoin into long-term yield until urgent payables are cleared."
        )
    else:
        st.error(
            f"{company_name} has elevated treasury risk. Upcoming payables are too close to available liquidity. "
            "The company should increase liquid stablecoin reserves before allocating more funds to yield."
        )

    st.subheader("Recommended Actions")

    recommendations = []

    if idle_liquidity > 0:
        recommendations.append(f"Review ${idle_liquidity:,.0f} as possible excess liquidity.")
    else:
        recommendations.append("Do not allocate more funds to yield until payments are covered.")

    if urgent_payables_usd > 0:
        recommendations.append(f"Prepare ${urgent_payables_usd:,.0f} for urgent payments due soon.")

    if funds_in_yield > total_balance * 0.5:
        recommendations.append("Reduce locked yield exposure because more than 50% of treasury is not fully liquid.")
    else:
        recommendations.append("Current yield allocation is within a reasonable range for a prototype scenario.")

    if edited_payables[edited_payables["Currency"] != "USD"].shape[0] > 0:
        recommendations.append("Monitor FX exposure because some payables are not in USD.")

    for item in recommendations:
        st.write(f"✅ {item}")

    st.subheader("AI CFO Summary")
    st.info(
        f"Based on current inputs, StableFlow classifies this treasury profile as **{risk_label}** "
        f"with a liquidity score of **{liquidity_score}/100**."
    )

# -----------------------------
# Tab 4: FX + Yield Simulator
# -----------------------------
with tab4:
    st.header("FX + Yield Simulator")

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("FX Exposure")
        fx_summary = edited_payables.groupby("Currency")["Amount"].sum().reset_index()
        fx_summary["USD Equivalent"] = fx_summary.apply(
            lambda row: row["Amount"] / fx_rates.get(row["Currency"], 1.0),
            axis=1
        )
        st.dataframe(fx_summary, use_container_width=True, hide_index=True)

        st.write("This shows how much the business needs to pay in each currency.")

    with c2:
        st.subheader("Yield Opportunity")
        st.dataframe(yield_options, use_container_width=True, hide_index=True)

        st.metric("Estimated Annual Yield", f"${annual_yield_estimate:,.0f}")
        st.metric("Estimated Monthly Yield", f"${monthly_yield_estimate:,.0f}")

    st.subheader("Yield Allocation Recommendation")

    if idle_liquidity > 0:
        safe_yield_amount = idle_liquidity * 0.6
        st.success(
            f"A conservative strategy could allocate around ${safe_yield_amount:,.0f} of excess liquidity "
            "to flexible yield, while keeping the rest available for payments."
        )
    else:
        st.warning(
            "No safe excess liquidity detected. The business should keep funds liquid instead of chasing yield."
        )

# -----------------------------
# Tab 5: Business Model
# -----------------------------
with tab5:
    st.header("Business Model")

    st.subheader("Revenue Model")
    st.dataframe(pricing, use_container_width=True, hide_index=True)

    st.subheader("Customer ROI Calculator")

    roi_col1, roi_col2, roi_col3 = st.columns(3)

    roi_col1.metric("Monthly Fee Savings", f"${monthly_fee_savings:,.0f}")
    roi_col2.metric("Monthly Yield Capture", f"${monthly_yield_estimate:,.0f}")
    roi_col3.metric("Estimated Monthly Value", f"${estimated_monthly_value:,.0f}")

    roi_df = pd.DataFrame({
        "Value Driver": ["Fee Savings", "Yield Capture"],
        "Monthly Value": [monthly_fee_savings, monthly_yield_estimate]
    })

    st.bar_chart(roi_df.set_index("Value Driver"))

    st.subheader("Go-To-Market Strategy")

    st.markdown(
        """
        **Initial target segment:** SMEs involved in cross-border trade, imports, exports, digital services, and logistics.

        **Beachhead market:** Businesses already holding stablecoins for supplier or vendor payments.

        **Acquisition channels:**

        - LinkedIn outreach to CFOs and founders
        - Partnerships with payment companies
        - Content around stablecoin treasury education
        - SME finance communities
        - Webinars on cross-border payment efficiency
        """
    )

    st.subheader("Competitive Positioning")
    st.info(
        "StableFlow is positioned between traditional SME finance software and complex DeFi tools. "
        "It is designed for business users who need clarity, not crypto complexity."
    )

# -----------------------------
# Tab 6: Final Project Summary
# -----------------------------
with tab6:
    st.header("Final Project Summary")

    st.subheader("Project Explanation")

    st.markdown(
        """
        StableFlow is a course project prototype for a stablecoin treasury dashboard.

        It helps small and medium-sized businesses manage:

        - USDC and USDT balances
        - Available liquidity
        - Upcoming supplier payables
        - FX exposure
        - Yield opportunities
        - AI-style treasury recommendations
        """
    )

    st.subheader("Tech Stack")

    st.write("- Python")
    st.write("- Streamlit")
    st.write("- Pandas")
    st.write("- GitHub")
    st.write("- Streamlit Cloud")

    st.subheader("Prototype Note")
    st.warning(
        "This is a prototype using mock data for educational purposes. "
        "It does not connect to real wallets, banks, exchanges, or DeFi protocols."
    )

    st.subheader("Pitch Closing Line")
    st.success(
        "StableFlow gives SMEs a simple way to manage stablecoin treasury decisions with the clarity of a CFO dashboard."
    )
