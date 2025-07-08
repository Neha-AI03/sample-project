# app.py

import streamlit as st
import sklearn
import pickle
import os

# Load trained model safely
MODEL_PATH = "flood_model.pkl"

if os.path.exists(MODEL_PATH):
    try:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    except ModuleNotFoundError as e:
        st.error("⚠️ Required module missing for loading the model:")
        st.code(str(e))
        st.stop()
    except Exception as e:
        st.error("🚫 An unexpected error occurred while loading the model:")
        st.code(str(e))
        st.stop()
else:
    st.error("📂 Model file 'flood_model.pkl' not found. Please make sure it's uploaded.")
    st.stop()

# Page setup
st.set_page_config(page_title="Smart Flood Alert System", layout="centered")

# Custom rain background
st.markdown("""
    <style>
    body {
        background-image: url('https://i.pinimg.com/originals/c1/1b/e5/c11be5eb4c6db331227d0147fcae0ab0.gif');
        background-size: cover;
        background-attachment: fixed;
    }
    .css-18e3th9 {
        background-color: rgba(255,255,255,0.9);
        padding: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title Slide
st.markdown("""
    <div style='text-align:center; padding:30px 0'>
        <h1 style='font-size: 55px; color: #003366;'>🌊 Smart Flood Alert System</h1>
        <h3>AI-Powered Prediction + Suraksha Bot + SMS Alert</h3>
        <p style='font-size: 18px;'>By <b>Flood Alert Team</b></p>
    </div>
""", unsafe_allow_html=True)

# Input Section
st.subheader("📥 Enter Weather Details")
rainfall = st.number_input("☔ Rainfall (mm)", min_value=0.0, step=1.0)
temperature = st.number_input("🌡️ Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, step=1.0)

# Predict
if st.button("🚨 Predict Flood Risk"):
    input_data = np.array([[rainfall, temperature, humidity]])
    result = model.predict(input_data)[0]

    if result == 1:
        st.error("🔴 Flood Likely! Please take precautions.")
        sms = "⚠️ सावधान! भारी वर्षा के कारण बाढ़ की संभावना है। कृपया सुरक्षित स्थान पर जाएं।"
        st.warning(f"📩 Hindi SMS Alert: {sms}")
    else:
        st.success("🟢 No Flood Risk Detected.")
        sms = "✅ कोई बाढ़ नहीं। आप सुरक्षित हैं।"
        st.info(f"📩 Hindi SMS Alert: {sms}")

# Chatbot Section
st.markdown("---")
st.subheader("🤖 Suraksha Bot - Your Flood & Weather Assistant")
query = st.text_input("💬 Ask something:")

if query:
    q = query.lower()
    if "flood" in q and "today" in q:
        st.write("🔍 I'm analyzing the flood risk based on today's input values. Click 'Predict Flood Risk' to know.")
    elif "flood" in q:
        st.write("🌊 Floods are caused by heavy rain and humidity. Stay alert during the monsoon season.")
    elif "safe" in q:
        st.write("🟢 You are safe if the system shows 'No Flood'. Always stay prepared.")
    elif "weather" in q or "temperature" in q:
        st.write(f"☁️ Today’s input: Rainfall = {rainfall} mm, Temp = {temperature}°C, Humidity = {humidity}%.")
    elif "yesterday" in q:
        st.write("🕓 Sorry, I can't access past data. Please input values manually if you have them.")
    elif "tomorrow" in q:
        st.write("📅 The system doesn’t predict tomorrow’s data. Please use forecast data.")
    elif "depth" in q:
        st.write("📏 Flood depth prediction is not available yet. Please refer to official weather departments.")
    elif "help" in q or "how" in q:
        st.write("✅ Move to higher ground, carry essentials, avoid floodwaters, and listen to official alerts.")
    elif "hello" in q or "hi" in q:
        st.write("👋 Hello! I'm Suraksha Bot, here to assist you with flood & weather queries.")
    elif "who" in q:
        st.write("🤖 I’m Suraksha Bot, your smart flood and weather assistant built by the Flood Alert Team.")
    elif "thank" in q:
        st.write("🙏 You're welcome. Stay safe!")
    else:
        st.write("🧠 I can answer flood, safety, and weather-related questions. Try asking about today's flood risk or safety tips.")

# Footer
st.markdown("---")
st.markdown("📘 _Stay Informed. Stay Safe. - Suraksha Bot_")

# Safety Checklist
st.markdown("---")
st.subheader("🛡️ Weather Safety Tips & Flood Checklist")

with st.expander("✅ Open Checklist"):
    st.markdown("""
    <div style='font-size: 17px; color: #003366;'>
        <ul>
            <li>📻 <b>Listen to weather updates</b> from official sources like IMD or NDMA.</li>
            <li>📦 <b>Prepare an emergency kit</b> – flashlight, medicines, dry food, water, important documents.</li>
            <li>🔋 <b>Keep phone and power bank charged</b> before heavy rainfall starts.</li>
            <li>🚪 <b>Move valuables to higher places</b> if water enters your area.</li>
            <li>💡 <b>Avoid walking or driving through floodwaters</b> – even 6 inches can knock you down!</li>
            <li>⛰️ <b>Move to higher ground immediately</b> if you hear sirens or alerts.</li>
            <li>🤝 <b>Help elderly and children</b> reach safety first.</li>
            <li>📲 <b>Use social media responsibly</b> to share verified information only.</li>
            <li>🚫 <b>Do not touch electrical lines</b> or fallen poles during rain.</li>
            <li>🚧 <b>Obey local authorities and evacuation orders</b> without delay.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
st.markdown("📘 _Stay Safe. Stay Alert. - Suraksha Bot_")
