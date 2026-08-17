import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="Flood Risk Classifier",
    page_icon="🌊",
    layout="centered"
)


# ============================================================
# LOAD MODEL
# ============================================================

# Project root: flood_risk_classifier/
BASE_DIR = Path(__file__).resolve().parent.parent

# Model files
MODEL_PATH = BASE_DIR / "models" / "flood_risk_model.pkl"
FEATURES_PATH = BASE_DIR / "models" / "model_features.pkl"


# Check model files
if not MODEL_PATH.exists():
    st.error(f"Model not found: {MODEL_PATH}")
    st.stop()

if not FEATURES_PATH.exists():
    st.error(f"Feature file not found: {FEATURES_PATH}")
    st.stop()


# Load model and feature names
model = joblib.load(MODEL_PATH)
feature_names = joblib.load(FEATURES_PATH)


# ============================================================
# TITLE
# ============================================================

st.title("🌊 Flood Risk Classifier")

st.write(
    "Enter the environmental, rainfall and drainage "
    "information below to predict flood risk.")


# ============================================================
# LOCATION
# ============================================================

st.header("📍 Location")

city_name = st.selectbox("City Name",["Osun, Nigeria", "Edo, Nigeria", "Rivers, Nigeria", "Kogi, Nigeria", "Lagos, Nigeria", "Colombo, Sri Lanka", "Chennai, India", "Delta, Nigeria", "Athens, Greece", "Others"])

latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=45.0)

longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=90.0)

elevation_m = st.number_input("Elevation (m)", min_value=-100.0, max_value=5000.0, value=500.0)


# ============================================================
# LAND AND SOIL
# ============================================================

st.header("🌱 Land & Soil")

land_use = st.selectbox("Land Use Type",["Residential", "Roads", "Commercial", "Green", "Industrial", "Mixed", "Institutional", "Water", "Informal", "Others"])

soil_group = st.selectbox("Soil Type",["A", "B", "C", "D"])


# ============================================================
# DRAINAGE
# ============================================================

st.header("🚧 Drainage")

drainage_density_km_per_km2 = st.number_input("Drainage Density (km/km²)", min_value=0.0, max_value=100.0, value=50.0)

storm_drain_proximity_m = st.number_input("Storm Drain Proximity (m)", min_value=0.0, max_value=1000.0, value=500.0)

storm_drain_type = st.selectbox("Storm Drain Type",["CurbInlet", "Manhole", "GratedInlet", "OpenChannel", "Others"])

drainage_efficiency = st.number_input("Drainage Efficiency", min_value=0.0, max_value=10.0, value=5.0)
# df["drainage_density_km_per_km2"]/(df["storm_drain_proximity_m"]+1)


# ============================================================
# RAINFALL
# ============================================================

st.header("🌧️ Rainfall")

historical_rainfall_intensity_mm_hr = st.number_input("Historical Rainfall Intensity (mm/hr)", min_value=0.0, max_value=500.0, value=100.0)

return_period_years = st.number_input("Return Period (Years)", min_value=0.0, max_value=100.0, value=50.0)

rainfall_per_return_period = st.number_input("Rainfall per Returns", min_value=0.0, max_value=100.0, value=50.0 )
# df["rainfall_per_return_period"]=df["historical_rainfall_intensity_mm_hr"]/(df["return_period_years"])

# ============================================================
# CREATE INPUT DATA
# ============================================================

input_df = pd.DataFrame([{
    "city_name": city_name,
    "latitude": latitude,
    "longitude": longitude,
    "elevation_m": elevation_m,
    "land_use": land_use,
    "soil_group": soil_group,
    "drainage_density_km_per_km2": drainage_density_km_per_km2,
    "storm_drain_proximity_m": storm_drain_proximity_m,
    "storm_drain_type": storm_drain_type,
    "historical_rainfall_intensity_mm_hr":historical_rainfall_intensity_mm_hr,
    "return_period_years": return_period_years,
    "drainage_efficiency": drainage_efficiency,
    "rainfall_per_return_period": rainfall_per_return_period
}])


# ============================================================
# PREDICTION
# ============================================================

if st.button("🌊 Predict Flood Risk", use_container_width=True):

    try:

        # Make sure input columns follow training order
        expected_features = list(feature_names)

        missing_features = [
            column
            for column in expected_features
            if column not in input_df.columns
        ]

        if missing_features:

            st.error(
                "The following model features are missing:"
            )

            st.write(missing_features)

            st.stop()

        input_df = input_df[expected_features]

        # Make prediction
        prediction = model.predict(input_df)[0]

        # Display result
        st.success(
            f"🌊 Predicted Flood Risk: **{prediction}**"
        )

    except Exception as error:

        st.error("An error occurred during prediction.")

        st.exception(error)
                         