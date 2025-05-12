import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Başlık ---
st.set_page_config(page_title="Enerji Tüketim Tahmin Sistemi", layout="centered")
st.title("Enerji Tüketimi Sınıflandırma Uygulaması")
st.markdown("Verilen verilerle aktif enerji kullanımını sınıflandırır.")

# --- Model ve Seçici Seçimi ---
model_names = ["KNN", "NaiveBayes", "MLP", "XGBoost"]
selector_names = ["PCA", "SelectKBest", "LDA"]

model_choice = st.selectbox("Model Seçin: (k-NN Dosya Boyutundan Ötürü İn-Aktif)", model_names)
selector_choice = st.selectbox("Özellik Seçici Seçin:", selector_names)

# --- Giriş Verileri ---
st.subheader("Giriş Özellikleri")
with st.form("input_form"):
    col1, col2 = st.columns(2)

    Global_active_power = col1.number_input("Global Active Power", value=1.0)
    Global_reactive_power = col1.number_input("Global Reactive Power", value=0.1)
    Voltage = col1.number_input("Voltage", value=240.0)
    Global_intensity = col1.number_input("Global Intensity", value=5.0)

    Sub_metering_1 = col2.number_input("Sub Metering 1", value=0.0)
    Sub_metering_2 = col2.number_input("Sub Metering 2", value=1.0)
    Sub_metering_3 = col2.number_input("Sub Metering 3", value=17.0)

    submitted = st.form_submit_button("Tahmin Et")

# --- Tahmin ---
if submitted:
    try:
        # 1. Model ve Seçici yükle
        model_path = f"pkl_models/{model_choice}_{selector_choice}.pkl"
        selector_path = f"pkl_models/{selector_choice}_selector.pkl"

        model = joblib.load(model_path)
        selector = joblib.load(selector_path)

        # 2. Veriyi ölçekle (aynı ölçeklemeyi varsayıyoruz)
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        dummy_X = pd.DataFrame([[Global_active_power, Global_reactive_power, Voltage,
                                 Global_intensity, Sub_metering_1, Sub_metering_2, Sub_metering_3]],
                               columns=["Global_active_power", "Global_reactive_power", "Voltage",
                                        "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"])
        dummy_X_scaled = scaler.fit_transform(dummy_X)

        # 3. Özellik dönüşümü uygula
        if selector_choice == "LDA":
            dummy_X_transformed = selector.transform(dummy_X_scaled)
        else:
            dummy_X_transformed = selector.transform(dummy_X_scaled)

        # 4. Tahmin et
        prediction = model.predict(dummy_X_transformed)[0]
        result_text = "**Yüksek Tüketim**" if prediction == 1 else "**Düşük Tüketim**"
        st.success(f"Tahmin Sonucu: {result_text}")

    except Exception as e:
        st.error(f"Hata oluştu: {str(e)}")
