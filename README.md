# 🧠 MindMate – Mental Health Risk Classifier

**MindMate** is a free, interactive web app built using **Streamlit** that helps users assess their mental health risk level based on workplace, lifestyle, and psychological factors. It uses a trained **machine learning model** to analyze your inputs and gives real-time suggestions along with curated video resources.

> ⚡ Try it out locally or deploy on Streamlit Cloud!

---

## 🔍 Features

### ✅ Mental Health Risk Prediction
- Users answer **22 simple questions** about work-life, personal habits, and mental well-being.
- The app uses a **Random Forest Classifier** to predict if the user is likely at **mental health risk** or not.

### 🧠 Smart Suggestions
- If risk is detected: users get personalized self-care tips (e.g., journaling, seeking help).
- If no risk is found: app shares wellness maintenance tips.

### 🎥 Embedded YouTube Videos
- Curated video content using `streamlit-player`:
  - Guided meditation
  - Relaxation techniques
  - Tips on improving work-life balance

### 🎨 Modern UI/UX
- Typing animation on header using CSS
- Animated illustrations powered by `streamlit-lottie`
- Styled buttons, consistent fonts, minimal layout

### 📚 Informative Pages
- **About Us**: Project mission + links to developer's GitHub & portfolio  
- **Donate Us**: Support via UPI with a clean and styled section

---

## 🧰 Tech Stack

- **Frontend/UI**: Streamlit, Lottie animations (`streamlit-lottie`), custom CSS
- **Model**: Scikit-learn (RandomForestClassifier)
- **Media Embeds**: `streamlit-player`
- **Extras**: Responsive sidebar navigation, minimal default menu

---

## 📦 Installation & Usage

### 🔧 Prerequisites
- Python 3.8+
- Install dependencies:

```bash
pip install -r requirements.txt





▶️ Run the app
bash
Copy
Edit
streamlit run app.py
📁 Project Structure
Copy
Edit
📦 MindMate/
 ┣ 📂 model/
 ┃ ┗ mental_health_model.pkl
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
💡 Future Enhancements
User session saving (optional login)

Feedback submission & mood journaling

Dark/light mode toggle

Multi-language support

🙋‍♂️ Author
Made with ❤️ by @kushfs
🔗 Portfolio

☕ Support
If you find this tool helpful, consider supporting its development:

📱 UPI: kushagrasinha140@okicici

📄 License
This project is open-source under the MIT License.

yaml
Copy
Edit

---

Would you also like a fancy project banner (PNG/Markdown) or badges (e.g. Streamlit app live, Python version, License, etc.)? I can add that too.










Tools


