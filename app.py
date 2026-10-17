import streamlit as st

st.set_page_config(
    page_title = "Perkly Pulse",
    page_icon = "📊",
    layout = "wide"
)

pages = {
    "workspace": [
        st.Page("pages/overview.py", title = "Overview", default = True),
        st.Page("pages/customers.py", title = "Customers"),
        st.Page("pages/transactions.py", title = "Transactions"),
        st.Page("pages/analytics_lab.py", title = "Analytics"),
        st.Page("pages/campaigns.py", title = "Campaigns"),
        st.Page("pages/loyalty_rewards.py", title = "Loyalty Rewards"),
        st.Page("pages/reports_data.py", title = "Reports"),
        st.Page("pages/system_health.py", title = "System Health")
    ]
}

selected_page = st.navigation(pages)
selected_page.run()