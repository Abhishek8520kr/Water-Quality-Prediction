# 💧 Water Quality Prediction using Machine Learning

This project builds a machine learning model to predict key water quality indicators based on chemical pollutant data. It aims to assist environmental monitoring efforts by providing faster, data-driven analysis of water health parameters.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Methodology](#methodology)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [Screenshots](#screenshots)
- [Conclusion](#conclusion)
- [License](#license)

---

## 🧠 Overview

The project analyzes chemical pollutant data from water bodies over time and predicts multiple water quality indicators using a machine learning model. This includes preprocessing date fields, feature extraction, and multi-output regression.

---

## ❓ Problem Statement

Ensuring access to safe and potable water is a major global challenge. Traditional water testing methods are time-consuming and costly. This project uses machine learning to predict water quality indicators from historical chemical data to enable faster, automated decision-making.

---

## 📊 Dataset

- **Source**: `PB_All_2000_2021.csv`
- **Features**: Includes chemical parameters recorded at various stations over time
- **Target Variables**:
  - Dissolved Oxygen (O₂)
  - Nitrate (NO₃)
  - Nitrite (NO₂)
  - Sulfate (SO₄)
  - Phosphate (PO₄)
  - Chloride (Cl⁻)

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib, Seaborn (for visualization)
- Scikit-learn
- Google Colab

---

## ⚙️ Methodology

1. **Data Collection**: Loaded CSV dataset with water quality data.
2. **Data Preprocessing**:
   - Converted date strings to `datetime` objects
   - Extracted `year` and `month` from date
   - Sorted by `station ID` and `date`
   - Handled missing values
3. **Feature Engineering**:
   - Selected relevant chemical features
   - Chose key pollutants as output variables
4. **Model Building**:
   - Used `RandomForestRegressor` wrapped in `MultiOutputRegressor` to handle multi-target regression
5. **Model Training**:
   - Split dataset into training and testing sets
   - Trained model on historical chemical measurements

---

## 📈 Model Evaluation

- **Metrics Used**:
  - R² Score (coefficient of determination)
  - Mean Squared Error (MSE)

These metrics were computed for each target variable.

---

## ✅ Results

- The model successfully predicted multiple water quality indicators simultaneously.
- Random Forest Regressor achieved solid performance with decent R² scores for most outputs.
- Demonstrated strong potential for real-world use in environmental monitoring systems.

---

## 🖼 Screenshots
> <img width="293" height="532" alt="image" src="https://github.com/user-attachments/assets/08f540ad-6720-469f-8ec6-a6c87ea8765b" />
> <img width="579" height="587" alt="image" src="https://github.com/user-attachments/assets/cc5c70d2-caca-4096-aacd-e19430b657fd" />



---

## 🧾 Conclusion

- Successfully developed a machine learning model to predict pollutant levels.
- Gained experience in multi-output regression and end-to-end ML workflow.
- This approach can complement traditional testing by offering faster, scalable insights.

---

## 🙋‍♂️ Author

**Abhishek Kumar**  
CSE (AI & ML) Graduate, 2025  
[LinkedIn](https://linkedin.com/in/your-profile)
