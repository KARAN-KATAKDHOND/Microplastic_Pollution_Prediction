# 🌊 Microplastic Pollution Prediction

A machine learning project aimed at predicting microplastic concentration levels in aquatic environments using environmental and anthropogenic factors.

## 📌 Project Overview
Microplastic pollution poses a serious threat to marine life, ecosystems, and human health. This project uses machine learning techniques to model and predict the concentration of microplastics in water bodies based on key environmental data.

## 🎯 Objectives
- Predict microplastic concentration using environmental and human-related features.
- Identify key contributing factors such as population density and industrial activity.
- Visualize and interpret the spatial patterns of pollution.
- Provide data-driven insights to support environmental monitoring and policy decisions.

## 🗃️ Dataset Overview
The dataset consists of ~5,000 records and includes:
- **Features:**  
  - Latitude, Longitude  
  - Water Temperature  
  - Salinity  
  - Depth  
  - Population Density (nearby area)  
  - Industrial Activity Index  
- **Target Variable:** Microplastic Concentration

> *Note: The dataset combines real-world research data and simulated values based on scientific trends.*

## 🧠 Methodology
- **Data Preprocessing:** Cleaning, normalization, handling missing values.
- **Exploratory Data Analysis:** Visualizations, correlation analysis.
- **Model Used:**  
  - **Linear Regression**  
    - Chosen for its simplicity, interpretability, and effectiveness with continuous data.
- **Model Evaluation:**  
  - **Metrics:** R² Score, RMSE  
  - Plots of actual vs predicted values for performance assessment.

## 📊 Results
- The model demonstrated reliable prediction performance.
- Key influencing factors identified include population density and industrial activity.
- Generated visual insights into high-risk pollution zones.

## 🔮 Future Work
- Integrate satellite imaging and time-series analysis.
- Extend prediction to estimate ecological impacts.
- Collaborate with environmental agencies for real-time monitoring.

## 💡 Conclusion
The project successfully showcases how machine learning can be applied to environmental data to predict and analyze microplastic pollution. The outcomes can aid researchers, policymakers, and conservation efforts.


## 🚀 How to Run the Project  

## ✅ Step 1: Install Python and Required Libraries  
Make sure you have Python installed, then install the dependencies:  
```bash
pip install -r requirements.txt
```

### ✅ Step 2: Run the Streamlit App  
Execute the following command to start the app:  
```bash
streamlit run app.py
```

### ✅ Step 3: App will Run on Localhost Port 8502  
Once the app starts, it will be available on **port 8502**.  

### ✅ Step 4: Open the App in Your Browser  
Go to:  
👉 [http://localhost:8502/](http://localhost:8502/)  

### ✅ Step 5: Use the App  
- Enter the required inputs.  
- Click the **Predict** button to see the final result.  

