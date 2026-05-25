import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# 1. THEMATIC STYLING & CORE BRANDING (Kalahari Theme)
# ==========================================
st.set_page_config(page_title="God's Herd / God se Kudde", page_icon="⛪", layout="wide")

# Custom CSS injection to match your exact visual presentation from the video
st.markdown("""
    <style>
    /* Main Background & Fonts */
    .stApp {
        background: linear-gradient(180deg, #3b0000 0%, #1a0000 100%);
        color: #ffffff;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Top Navigation Simulation Bar */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: rgba(255, 255, 255, 0.05);
        padding: 0.8rem 2rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 2rem;
    }
    .top-nav-brand {
        font-size: 1.5rem;
        font-weight: bold;
        color: #ff9f43;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Elegant Custom Headers */
    .main-header {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: 2px;
        color: #ffffff;
        text-transform: uppercase;
        margin-top: 1rem;
        margin-bottom: 0px;
    }
    .sub-header {
        text-align: center;
        font-size: 1.2rem;
        color: #ff9f43;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 3rem;
    }
    
    /* Grid Layout Interactive Cards */
    .committee-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.2s;
        margin-bottom: 1.5rem;
        min-height: 220px;
    }
    .committee-card:hover {
        transform: translateY(-5px);
    }
    .committee-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .committee-title {
        color: #1a0000 !important;
        font-size: 1.4rem !important;
        font-weight: bold !important;
        margin-bottom: 0.5rem;
    }
    .committee-subtitle {
        color: #666666;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Info Display Banners */
    .banner-box {
        background: linear-gradient(90deg, #ea580c 0%, #ff9f43 100%);
        padding: 2.5rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2.5rem;
        box-shadow: 0 6px 20px rgba(234, 88, 12, 0.2);
    }
    .banner-text {
        font-size: 2.5rem;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    /* Calendar Grid Matrix Styles */
    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 8px;
        margin-bottom: 2rem;
    }
    .calendar-day {
        background-color: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 12px;
        text-align: left;
        min-height: 80px;
    }
    .calendar-day-header {
        font-weight: bold;
        color: #ff9f43;
    }
    .calendar-day-event {
        font-size: 0.75rem;
        background-color: #ea580c;
        color: white;
        padding: 2px 6px;
        border-radius: 4px;
        margin-top: 5px;
        display: inline-block;
    }
    
    /* Native Overrides for Streamlit Elements to fit dark mode template */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(0,0,0,0.2);
        padding: 8px;
        border-radius: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #ffffff !important;
        font-weight: bold;
        padding: 10px 20px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #ea580c !important;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SESSION STATE & ADMINISTRATIVE LEDGER MEMORIES
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = None

if 'members_archive' not in st.session_state:
    st.session_state.members_archive = pd.DataFrame([
        {"ID": 101, "First Name": "Johannes", "Last Name": "Willemse", "Wyk": "Kameelmond", "Status": "Belydende Lidmaat"},
        {"ID": 102, "First Name": "Ryan", "Last Name": "Willemse", "Wyk": "Central Town", "Status": "Dooplidmaat"},
        {"ID": 103, "First Name": "Dean", "Last Name": "Willemse", "Wyk": "Central Town", "Status": "Dooplidmaat"}
    ])

MASTER_PIN = "pete-master-admin"

# ==========================================
# 3. TOP LEVEL NAVIGATION (Simulated Horizontal Header)
# ==========================================
st.markdown("""
    <div class="top-nav">
        <div class="top-nav-brand">⛪ God se Kudde</div>
        <div style="font-size: 0.9rem; color: #ff9f43; font-weight: bold;">📍 UPINGTON, NORTHERN CAPE</div>
    </div>
""", unsafe_allow_html=True)

# Main Structural Section Menus via Streamlit Sidebar
st.sidebar.image("https://img.icons8.com/color/96/chapel.png", width=80)
st.sidebar.markdown("### KONINGKRYK PORTAL")

section = st.sidebar.radio(
    "Gaan Na:",
    ["🏡 Welkom Tuis", "📅 Kerk-Kalender", "💰 Offergawes", "🏛️ Kerk-Komitees", "⚙️ Administrasie Panel"]
)

st.sidebar.markdown("---")
if st.session_state.logged_in:
    st.sidebar.success(f"Clearance: MASTER ADMIN")
    if st.sidebar.button("🔒 Sluit Stelsel"):
        st.session_state.logged_in = False
        st.session_state.user_role = None
        st.rerun()

# ==========================================
# MODULE 1: WELKOM TUIS (Landing Dashboard)
# ==========================================
if section == "🏡 Welkom Tuis":
    st.markdown('<p class="main-header">God se Kudde</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">VREDE OPINGTON</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.icons8.com/illustrations/external-kmg-design-flat-kmg-design/250/external-church-easter-day-kmg-design-flat-kmg-design.png", use_container_width=True)
    with col2:
        st.markdown("### Welkom by Ons Digitale Gemeenskap")
        st.info("Hier bou ons saam as lidmate, gee met blymoedigheid, en bestuur ons wyke met orde en deursigtigheid. Gebruik die linkerkantste kieslys om deur die komitees, kalender, en registers te navigeer.")
        st.markdown("""
        **Kontak Besonderhede:**
        * 📞 Tel: +27 54 332 1100
        * ✉️ E-pos: info@godsekuddeupington.co.za
        * 📍 Adres: Upington, Northern Cape, South Africa
        """)

# ==========================================
# MODULE 2: KERK-KALENDER (Dynamic Matrix Grid)
# ==========================================
elif section == "📅 Kerk-Kalender":
    st.markdown('<p class="main-header">Kerk-Kalender</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Sondagdienste • Bybelstudies • Vergaderings</p>', unsafe_allow_html=True)
    
    st.markdown("### Mei / Junie 2026")
    
    # Building the clean calendar day boxes from your design profile
    st.markdown("""
        <div class="calendar-grid">
            <div class="calendar-day"><span class="calendar-day-header">Ma 18</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Di 19</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Wo 20</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Do 21</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Vr 22</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Sa 23</span><br><span class="calendar-day-event">Gebedstudie</span></div>
            <div class="calendar-day"><span class="calendar-day-header">So 24</span><br><span class="calendar-day-event">Oggenddiens 09:00</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Ma 25</span><br><span class="calendar-day-event">Vandag</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Di 26</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Wo 27</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Do 28</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Vr 29</span></div>
            <div class="calendar-day"><span class="calendar-day-header">Sa 30</span></div>
            <div class="calendar-day"><span class="calendar-day-header">So 31</span><br><span class="calendar-day-event">Pinkster Fees</span></div>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODULE 3: OFFERGAWES (Presentation Slider Banner)
# ==========================================
elif section == "💰 Offergawes":
    st.markdown('<div class="banner-box"><div class="banner-text">Offergawes</div><div style="color:white; opacity:0.9;">"God het 'n blymoedige gewer lief."</div></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Bankbesonderhede")
        st.markdown("""
        * **Bank:** Eerste Nasionale Bank (FNB)
        * **Rekeningnaam:** God se Kudde Upington
        * **Rekeningnommer:** 62991122334
        * **Takkode:** 250655
        * **Verwysing:** *U Naam / Wyk*
        """)
    with col2:
        st.markdown("### Tipes Bydraes")
        st.success("💵 **Dankoffers:** Maandelikse of weeklikse danksegging.")
        st.warning("🤝 **Kollektekas:** Fondse geoormerk vir gemeenskapsuitreike in Louisvale en Kalksloot.")

# ==========================================
# MODULE 4: KERK-KOMITEES (Visual Card Interfaces)
# ==========================================
elif section == "🏛️ Kerk-Komitees":
    st.markdown('<p class="main-header">Kerk-Komitees</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Strukture en Werksgroepe</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="committee-card">
                <div class="committee-icon">📋</div>
                <div class="committee-title">PAK</div>
                <div class="committee-subtitle">Program, Administrasie & Kommunikasie</div>
                <p style="color:#555555; font-size:0.9rem; margin-top:10px;">Verantwoordelik vir bulletins en herstelbijeenkomste.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Sien PAK Inligting"):
            st.info("Die PAK komitee koördineer die herstelgebede vir die Kameelmond kerkgebou.")
            
    with col2:
        st.markdown("""
            <div class="committee-card">
                <div class="committee-icon">📅</div>
                <div class="committee-title">Reëlingskomitee</div>
                <div class="committee-subtitle">Eredienste & Spesiale Funksies</div>
                <p style="color:#555555; font-size:0.9rem; margin-top:10px;">Sien om na die logistiek van die oggenddienste.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Sien Reëlings"):
            st.info("Behartig die altuargrafie en sangborde vir die Sondag oggenddiens.")
            
    with col3:
        st.markdown("""
            <div class="committee-card">
                <div class="committee-icon">🔑</div>
                <div class="committee-title">Eiendomskommissie</div>
                <div class="committee-subtitle">Fasiliteite & Bates</div>
                <p style="color:#555555; font-size:0.9rem; margin-top:10px;">In stand hou van bates en infrastruktuur.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Sien Bates"):
            st.info("Toesig oor die fisiese geboue en toerusting in die Upington streek.")

# ==========================================
# MODULE 5: ADMINISTRASIE PANEL (Secure Gateway Gate)
# ==========================================
elif section == "⚙️ Administrasie Panel":
    st.markdown('<p class="main-header">Administrasie</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Lidmaat Register & Data Integriteit</p>', unsafe_allow_html=True)
    
    # Gatekeeper check for Pete's Master Overwriting Password
    if not st.session_state.logged_in:
        st.markdown("### 🔒 Geslote Bestuursterminaal")
        pin_input = st.text_input("Voer Magtigingskode in", type="password", placeholder="••••")
        
        if st.button("Verifieer Sekuriteitsleutel"):
            if pin_input == MASTER_PIN:
                st.session_state.logged_in = True
                st.session_state.user_role = "master_admin"
                st.success("Magtiging Suksesvol! Welkom terug, Pete.")
                st.rerun()
            else:
                st.error("Ongeldige PIN-kode. Toegang Geweier.")
    else:
        st.success("⚡ VOLLE ADMINISTRATIEWE KLARING TOEGESTAAN")
        
        tab1, tab2 = st.tabs(["🔍 Lidmaat Register Data", "✍️ Nuwe Inskrywing (Voeg By)"])
        
        with tab1:
            st.markdown("### Aktiewe Lidmaat Argief Ledger")
            search_query = st.text_input("Filter rekords volgens naam of wyk:")
            df = st.session_state.members_archive
            if search_query:
                df = df[df.astype(str).apply(lambda x: x.str.contains(search_query, case=False)).any(axis=1)]
            st.dataframe(df, use_container_width=True)
            
        with tab2:
            st.markdown("### Nuwe Profiel Vaslegging")
            with st.form("capture_form_pete", clear_on_submit=True):
                f_name = st.text_input("Voornaam")
                l_name = st.text_input("Van")
                wyk = st.selectbox("Toegewysde Wyk / Ward", ["Kameelmond", "Louisvale", "Kalksloot", "Central Town"])
                status = st.selectbox("Status / Kerkbelydenis", ["Belydende Lidmaat", "Dooplidmaat"])
                
                submit_entry = st.form_submit_button("Commit Veranderinge")
                if submit_entry:
                    if f_name and l_name:
                        new_id = st.session_state.members_archive["ID"].max() + 1
                        new_row = {"ID": new_id, "First Name": f_name, "Last Name": l_name, "Wyk": wyk, "Status": status}
                        st.session_state.members_archive = pd.concat([st.session_state.members_archive, pd.DataFrame([new_row])], ignore_index=True)
                        st.success(f"Databaselys suksesvol opgedateer vir: {f_name} {l_name}.")
                        st.rerun()
                    else:
                        st.error("Velde mag nie leeg gelaat word 