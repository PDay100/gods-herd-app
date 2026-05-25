import streamlit as st
import pandas as pd
from datetime import datetime

# 1. THEMATIC STYLING & PAGE INITIALIZATION
st.set_page_config(page_title="God's Herd / God se Kudde", page_icon="⛪", layout="wide")

# Fixed styling loader for current Streamlit/Python environments
st.markdown("""
    <style>
    .main { background-color: #fffaf5; }
    h1, h2, h3 { color: #c2410c !important; font-family: 'Sans-Serif'; }
    .stButton>button {
        background-color: #ea580c;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #c2410c; color: white; }
    .sidebar .sidebar-content { background-color: #ffedd5; }
    </style>
""", unsafe_allow_html=True)

# 2. SECURE ACCESS CONTROL & SESSION MANAGEMENT
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.user_fullname = ""

if 'members_archive' not in st.session_state:
    st.session_state.members_archive = pd.DataFrame([
        {"ID": 101, "First Name": "Johannes", "Last Name": "Willemse", "Wyk": "Kameelmond", "Status": "Belydende Lidmaat"},
        {"ID": 102, "First Name": "Ryan", "Last Name": "Willemse", "Wyk": "Central Town", "Status": "Dooplidmaat"},
        {"ID": 103, "First Name": "Dean", "Last Name": "Willemse", "Wyk": "Central Town", "Status": "Dooplidmaat"}
    ])

MASTER_PIN = "pete-master-admin"

# 3. PORTAL ACCESSIBILITY GATEWAY (Login Screen)
if not st.session_state.logged_in:
    st.title("⛪ God's Herd / God se Kudde")
    st.subheader("Secure Church Management Gateway")
    st.markdown("---")
    
    st.markdown("### Access Authentication")
    
    if st.button("🌐 Continue with Google Sign-In"):
        st.session_state.logged_in = True
        st.session_state.user_role = "member"
        st.session_state.user_fullname = "Church Member (Google Verified)"
        st.rerun()
        
    st.markdown("---")
    st.markdown("#### Staff & Management Secure Terminal PIN")
    
    user_pin = st.text_input("Enter secure access code", type="password", placeholder="••••")
    if st.button("Verify Security Code"):
        if user_pin == MASTER_PIN:
            st.session_state.logged_in = True
            st.session_state.user_role = "master_admin"
            st.session_state.user_fullname = "Pete-Dawid Willemse (Master Architect)"
            st.rerun()
        elif user_pin == "eldr-view-2026":
            st.session_state.logged_in = True
            st.session_state.user_role = "elder"
            st.session_state.user_fullname = "Church Elder / Ouderling"
            st.rerun()
        else:
            st.error("Invalid security signature. Access denied.")
            
    st.stop()

# 4. APPLICATION CORE DASHBOARD
st.sidebar.markdown(f"### Logged in as:\n**{st.session_state.user_fullname}**")
st.sidebar.markdown(f"Clearance Level: `{st.session_state.user_role.upper()}`")

if st.sidebar.button("🔒 Secure Logout"):
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.user_fullname = ""
    st.rerun()

st.sidebar.markdown("---")
menu = st.sidebar.radio("Navigation Menu", ["📢 Announcements", "👥 Archive Registry"])

if menu == "📢 Announcements":
    st.title("PAK Communication Board")
    st.info("**Weekly Bulletin:** Joint restoration prayers scheduled for Kameelmond Church building this coming Saturday at 09:00.")

elif menu == "👥 Archive Registry":
    st.title("Church Archival Profile Registry")
    
    if st.session_state.user_role in ["member", "elder"]:
        st.warning("⚠️ SECURITY NOTICE: You have view-only access to this ledger. Data modifications are strictly restricted to the Master System Administrator.")
        
        st.markdown("### Searchable Member Records")
        search_query = st.text_input("🔍 Search Archive records by name or ward")
        df = st.session_state.members_archive
        if search_query:
            df = df[df.astype(str).apply(lambda x: x.str.contains(search_query, case=False)).any(axis=1)]
        st.dataframe(df, use_container_width=True)

    elif st.session_state.user_role == "master_admin":
        st.success("⚡ ADMINISTRATIVE CLEARANCE GRANTED: Full write capabilities unlocked.")
        
        tab1, tab2 = st.tabs(["🔍 Database Records Viewer", "✍️ Append / Update Registry (Pete Only)"])
        
        with tab1:
            st.markdown("### Master Ledger System")
            st.dataframe(st.session_state.members_archive, use_container_width=True)
            
        with tab2:
            st.markdown("### Capture New Historical Profile")
            with st.form("admin_capture_form", clear_on_submit=True):
                f_name = st.text_input("First Name")
                l_name = st.text_input("Last Name")
                wyk = st.selectbox("Assigned Wyk / Ward", ["Kameelmond", "Louisvale", "Kalksloot", "Central Town"])
                status = st.selectbox("Status", ["Belydende Lidmaat", "Dooplidmaat"])
                
                submit_entry = st.form_submit_button("Commit Changes Permanently")
                if submit_entry:
                    if f_name and l_name:
                        new_id = st.session_state.members_archive["ID"].max() + 1
                        new_row = {"ID": new_id, "First Name": f_name, "Last Name": l_name, "Wyk": wyk, "Status": status}
                        st.session_state.members_archive = pd.concat([st.session_state.members_archive, pd.DataFrame([new_row])], ignore_index=True)
                        st.success(f"Database block updated successfully. Record saved for {f_name} {l_name}.")
                        st.rerun()
                    else:
                        st.error("Fields cannot be left empty during master override logs.")