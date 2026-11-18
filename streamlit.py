import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Product Review Sentiment Analyzer")
st.write("Enter a product review and get instant sentiment prediction!")

# Input box
review = st.text_area("Enter your product review here:", height=150)

# Predict button
if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            # Call your Flask backend
            response = requests.post(
                "https://sentimental-analysis-7en7.onrender.com/predict",
                json={"reviews": review}
            )

            result = response.json()

            # Display result

            sentiment = result['prediction']
            # confidence = result['confidence']
            if 'positive' in sentiment or 'negative' in sentiment:
                st.success(f'Sentiment : {sentiment}')
            else:
                st.error(f'Sentiment : {sentiment}')
            # st.metric(Label='Confidence',value=confidence)
            
