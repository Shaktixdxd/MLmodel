
import streamlit as st

# Set page title
st.title("ML Disease Model")

# List of symptoms (replace with your 132 symptoms)
symptoms = [
    "Abdominal Pain", "Abnormal Menstruation", "Acidity", "Acute Liver Failure", "Altered Sensorium", "Anxiety", 
    "Back Pain", "Belly Pain", "Blackheads", "Blister", "Blood in Sputum", "Bloody Stool", "Blurred and Distorted Vision", 
    "Breathlessness", "Brittle Nails", "Burning Micturition", "Chills", "Cold Hands and Feets", "coma", "Congestion", 
    "Constipation", "Continuous Feel of Urine", "Continuous Sneezing", "Cough", "Cramps", "Dark Urine", "Dehydration", 
    "Depression", "Diarrhoea", "Dischromic Patches", "Dizziness", "Drying and Tingling Lips", "Enlarged Thyroid", 
    "Excessive Hunger", "Extra Marital Contacts", "Family History", "Fast Heart Rate", "Fatigue", "Fluid Overload", 
    "Foul Smell of Urine", "Frequent Urination", "High Fever", "History of Alcohol Consumption", "Hip Joint Pain", 
    "Irritability", "Irritation in Anus", "Itching", "Joint Pain", "Knee Pain", "Lack of Concentration", "Lethargy", 
    "Loss of Appetite", "Loss of Balance", "Loss of Smell", "Malaise", "Mood Swings", "Movement Stiffness", "Muscle Pain", 
    "Muscle Weakness", "Muscle Wasting", "Mucoid Sputum", "Nausea", "Neck Pain", "Nodal Skin Eruptions", "Obesity", 
    "Pain Behind the Eyes", "Pain During Bowel Movements", "Pain in Anal Region", "Painful Walking", "Palpitations", 
    "Passage of Gases", "Phlegm", "Polyuria", "Prominent Veins on Calf", "Puffy Face and Eyes", "Pus Filled Pimples", 
    "Rapid Heart Rate", "Red Sore Around Nose", "Red Spots Over Body", "Receiving Blood Transfusion", 
    "Receiving Unsterile Injections", "Restlessness", "Rusty Sputum", "Runny Nose", "Scarring", "Shivering", 
    "Silver Like Dusting", "Sinus Pressure", "Skin Peeling", "Skin Rash", "Small Dents in Nails", "Spinning Movements", 
    "Spotting Urination", "Stiff Neck", "Stomach Bleeding", "Stomach Pain", "Sudden High Fever", "Sunken Eyes", "Sweating", 
    "Swelling Joints", "Swelling of Stomach", "Swollen Blood Vessels", "Swollen Extremities", "Swollen Legs", "Throat Irritation", 
    "Toxic Look (Typhos)", "Ulcers on Tongue", "Unsteadiness", "Visual Disturbances", "Vomiting", "Watering from Eyes", 
    "Weakness in Limbs", "Weakness of One Body Side", "Weight Gain", "Weight Loss", "Yellow Crust Ooze", "Yellowing of Eyes", "Yellowish Skin"
]

# Dictionary to store checkbox values
checkbox_values = {}

# Display symptom checkboxes
for symptom in symptoms:
    checkbox_values[symptom] = st.number_input(f"{symptom}:", min_value=0, max_value=1, value=0, step=1, key=symptom)

# Save button
if st.button("Save"):
    selected_symptoms = [symptom for symptom, value in checkbox_values.items() if value == 1]
    selected_symptoms.sort()
    output_string = ", ".join(selected_symptoms)
    st.text_area("Selected Symptoms:", value=output_string, height=100)

