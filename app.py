import streamlit as st
import numpy as np
import pickle

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Sales Prediction Dashboard",
    page_icon="📊",
    layout="wide",
)

# ======================================================
# LOAD MODEL
# ======================================================
model = pickle.load(open(r"D:\\data_science_repo\\Sales\\model.pkl", "rb"))

# ======================================================
# CUSTOM CSS
# ======================================================
st.markdown("""
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background */
[data-testid="stAppViewContainer"]{
    background: linear-gradient(
        135deg,
        #0B1120 0%,
        #111827 40%,
        #1E293B 100%
    );
}

/* Remove Streamlit Header */
[data-testid="stHeader"]{
    background: transparent;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background: #0F172A;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Sidebar Text */
[data-testid="stSidebar"] *{
    color:#E2E8F0 !important;
}

/* General Text */
h1,h2,h3,h4,h5,h6{
    color:#F8FAFC !important;
}

p,label,span{
    color:#CBD5E1 !important;
}

/* Header Card */
.dashboard-header{
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(15px);
    border-radius: 24px;
    padding: 35px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.08);
    box-shadow:0px 10px 30px rgba(0,0,0,0.25);
    margin-bottom:30px;
}

.dashboard-title{
    font-size:48px;
    font-weight:700;
    color:#F8FAFC;
}

.dashboard-subtitle{
    font-size:18px;
    color:#94A3B8;
}

/* KPI Cards */
.metric-card{
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius:20px;
    padding:25px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.08);
    box-shadow:0px 8px 20px rgba(0,0,0,0.25);
    transition:all .3s ease;
}

.metric-card:hover{
    transform:translateY(-5px);
}

.metric-title{
    color:#94A3B8;
    font-size:15px;
    font-weight:500;
}

.metric-value{
    color:#F8FAFC;
    font-size:28px;
    font-weight:700;
    margin-top:10px;
}

/* Prediction Card */
.prediction-card{
    background: linear-gradient(
        135deg,
        #2563EB,
        #7C3AED
    );
    border-radius:25px;
    padding:40px;
    text-align:center;
    color:white;
    margin-top:20px;
    box-shadow:0px 15px 35px rgba(37,99,235,0.35);
}

.prediction-title{
    font-size:22px;
    font-weight:500;
}

.prediction-value{
    font-size:60px;
    font-weight:700;
    margin-top:10px;
}

/* Button */
.stButton > button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    background:linear-gradient(
        90deg,
        #06B6D4,
        #2563EB
    );
    color:white;
    font-size:18px;
    font-weight:600;
    box-shadow:0px 8px 20px rgba(37,99,235,0.35);
}

.stButton > button:hover{
    transform:translateY(-2px);
}

/* Footer */
.footer{
    text-align:center;
    color:#64748B;
    margin-top:40px;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# HEADER
# ======================================================
st.markdown("""
<div class="dashboard-header">
    <div class="dashboard-title">
        📊 Sales Prediction Dashboard
    </div>
    <div class="dashboard-subtitle">
        AI-Powered Sales Forecasting & Business Intelligence
    </div>
</div>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR INPUTS
# ======================================================
with st.sidebar:

    st.header("⚙️ Input Parameters")

    category_map = {
        "Electronics": 1,
        "Furniture": 2,
        "Clothing": 3,
        "Sports": 4,
        "Food": 5
    }

    selected_category = st.selectbox(
        "📦 Product Category",
        options=list(category_map.keys())
    )

    Product_Category = category_map[selected_category]

    Quantity = st.slider(
        "🔢 Quantity",
        min_value=1,
        max_value=100,
        value=10
    )

    Price_per_Unit = st.slider(
        "💰 Price Per Unit (₹)",
        min_value=10,
        max_value=5000,
        value=500,
        step=10
    )

# ======================================================
# KPI SECTION
# ======================================================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📦 Product Category</div>
        <div class="metric-value">{selected_category}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🔢 Quantity</div>
        <div class="metric-value">{Quantity}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💰 Unit Price</div>
        <div class="metric-value">₹ {Price_per_Unit:,}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ======================================================
# PREDICTION
# ======================================================
st.subheader("📈 Sales Forecast")

if st.button("🚀 Predict Sales"):

    input_data = np.array([
        [
            Product_Category,
            Quantity,
            Price_per_Unit
        ]
    ])

    prediction = model.predict(input_data)

    st.markdown(f"""
    <div class="prediction-card">
        <div class="prediction-title">
            Predicted Sales Revenue
        </div>
        <div class="prediction-value">
            ₹ {prediction[0]:,.2f}
        </div>
        <p>
            Estimated revenue based on the selected inputs
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

# ======================================================
# FOOTER
# ======================================================
st.markdown("""
<div class="footer">
    © 2026 Sales Prediction Dashboard • Machine Learning Powered • Built with Streamlit
</div>
""", unsafe_allow_html=True)