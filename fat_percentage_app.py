import streamlit as st
import pandas as pd
import joblib

# --- بارگذاری مدل ذخیره‌شده ---
model = joblib.load("fat_percentage_predictor.joblib")

# --- عنوان اپ ---
st.title("🔮 پیش‌بینی درصد چربی بدن")
st.write(".این اپ با استفاده از مدل یادگیری ماشین، درصد چربی بدن شما را پیش‌بینی می‌کند")

# --- گرفتن ورودی‌های کاربر ---
age = st.number_input("سن (سال)", min_value=10, max_value=100, value=28)
gender = st.selectbox("جنسیت", ["Male", "Female"])
weight = st.number_input("وزن (kg)", min_value=30.0, max_value=200.0, value=80.0)
height = st.number_input("قد (m)", min_value=1.0, max_value=2.5, value=1.78)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.2)
workout_type = st.selectbox("نوع تمرین", ["Cardio", "Strength", "HIIT", "Yoga"])
workout_freq = st.number_input("تعداد روزهای تمرین در هفته", min_value=0, max_value=7, value=4)
session_duration = st.number_input("مدت تمرین در هر جلسه (ساعت)", min_value=0.0, max_value=5.0, value=1.0)
calories_burned = st.number_input("کالری سوخته شده در تمرین", min_value=0, max_value=5000, value=450)
daily_calories = st.number_input("کل کالری دریافتی روزانه", min_value=1000, max_value=5000, value=2200)
carbs = st.number_input("کربوهیدرات روزانه (گرم)", min_value=0, max_value=1000, value=240)
proteins = st.number_input("پروتئین روزانه (گرم)", min_value=0, max_value=500, value=120)
fats = st.number_input("چربی روزانه (گرم)", min_value=0, max_value=300, value=60)
water_intake = st.number_input("مقدار آب مصرفی روزانه (لیتر)", min_value=0.0, max_value=10.0, value=2.5)
experience_level = st.selectbox("سطح تجربه تمرینی", [1, 2, 3], format_func=lambda x: {1:"Beginner",2:"Intermediate",3:"Advanced"}[x])

# --- دکمه پیش‌بینی ---
if st.button("پیش‌بینی درصد چربی"):
    new_user = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Weight (kg)": weight,
        "Height (m)": height,
        "BMI": bmi,
        "Workout_Type": workout_type,
        "Workout_Frequency (days/week)": workout_freq,
        "Session_Duration (hours)": session_duration,
        "Calories_Burned": calories_burned,
        "Calories": daily_calories,
        "Carbs": carbs,
        "Proteins": proteins,
        "Fats": fats,
        "Water_Intake (liters)": water_intake,
        "Experience_Level": experience_level
    }])

    prediction = model.predict(new_user)[0]
    st.success(f"🔹 درصد چربی پیش‌بینی‌شده: {prediction:.2f}درصد")
