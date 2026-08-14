# FLOOD RISK CLASSIFIER

## Project Overview:
Flooding is a major environmental challenge in Nigeria and other flood prone rregions. This project makes use of machine
learning approach to classify flood risks based on environmental/geographical locations, rainfall and drainage related
factors. This project develops a multiclass classification model that predicts flood risk categories such as Low Risk,
Medium Risk and Extreme Risk. This system is designed to demonstrate how machine learning can support flood risk
assessments and proactive decision making steps for communities , emmergency planners, NGOs, government bodies and other
stakeholders.

## Project Objective:
The main objective of this project is to develop a machine learning model capable of predicting flood risk levels from
relevant environmental and infrastructure related features.

## Problem Type:
Multiclass Classification

## Target Variable:
The original target variable is: "risk_labels". The original or raw dataset contains numerous detailed risk labels. These
would be simplified into broader flood risk categories (Low Risk, Medium Risk and High Risk) for machine learning
classification.

## Features Used:
The model uses environmental, geographical, rainfall and drainage related features. These features include:
- City Name
- Latitude
- Longitude
- Elevation
- Land Use
- Soil Group
- Drainage Density (km/km²)
- Storm Drain Proximity (m)
- Storm Drain Type
- Historical Rainfall Intensity (mm/hr)
- Return Period (Years)
- Drainage Efficiency ([drainage_density_km_per_km2]/[storm_drain_proximity_m]+1)
- Rainfall per Returns ([historical_rainfall_intensity_mm_hr"]/[return_period_years])

## Machine Learning Workflow:
The project follows a standard machine learning workflow:
1. Identifying the Problem
2. Data sourcing/collection
3. Data cleaning
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Target Variable Transformation
7. Feature Selection
8. Data Splitting
9. Model Training
10. Model Evaluation
11. Best Model Selection
12. Model Saving
13. Streamlit Deployment

## Data Preprocessing
The dataset was examined for:
- Missing values
- Duplicate records
- Categorical variables
- Numerical variables
- Class distribution
- Outliers
- Feature relationships
Categorical variables were processed appropriately before model training.
The original risk labels were simplified into broader flood-risk categoriesto make the classification problem more
manageable.

## Machine Learning Model
The project uses supervised machine learning for multiclass flood-risk classification. The trained model is saved using
joblib: "flood_risk_model.pkl"
The features used during model training are saved separately as: "model_features.pkl"

## Model Evaluation
Three models were trained and evaluated using appropriate classification metrics, including;
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
And the best performing model was chosen. These metrics were used to to assess the models' ability to correctly classify
different flood-risk categories

## Potential Applications
The flood-risk classifier could potentially support:
- Flood-risk assessment
- Emergency planning
- Community awareness
- Disaster preparedness
- Environmental planning
- Infrastructure planning
- NGO intervention planning
- Local government decision-making
This model should be considered as a decision-support tool rather than a replacement for professional hydrological or
emergency-management assessments.

## Future Improvements
Areas for potential improvements include:
- Incorporating real-time rainfall data
- Incorporating river water-level data
- Using satellite imagery
- Adding historical flood-event data
- Incorporating soil moisture data
- Testing additional machine learning algorithms
- Hyperparameter optimization
- Improving class balance
- Deploying a GIS-based flood-risk visualization system

## Technologies Used
- Anaconda
- Jupyter Notebook
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

## How to Run the Notebook and Streamlit App
1. Activate the Environment: Open Anaconda Prompt; "conda activate venv"
2. Navigate to the Project Root: "cd "C:\Users\User\fllood_risk_classifier"". Ensure you are in the project root containing app, data, model, notebook, requirements.txt, README.md
3. Install the Required Packages: If the packages have not been installed: "pip install -r requirwmwnts.txt"
4. Launch Jupyter Notebook: Run "jupyter notebook"
5. From the project root file, navigate to "notebook", then open "Flood Risk Classifier.ipynb"
6. Run the Notebook: Run the cells sequentially from the beginning as the notebook covers major stages of the machine learning workflow.
7. Back to the Anaconda Prompt Terminal, Ctrl+C to stop the current operation process
8. Ensure you are still on the Project Root: Run "streamlit run app/app.py"
9. Streamlit will redirect you to your web browser while also provide you with a local host link which grants you access to the application.

## Disclaimer
This project is developed for educational and demonstration purposes. Predictions generated by this model should
not be treated as an official flood warning or as a substitute for professional hydrological, meteorological,
engineering or emergency-management assessments.
