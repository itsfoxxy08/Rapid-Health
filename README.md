# Rapid-Health (QuickMed)

Rapid-Health (QuickMed) is an AI-assisted health triage tool designed to provide quick, preliminary symptom interpretation. It uses natural-language understanding to analyze user-entered symptoms and returns the most probable condition based on similarity scores. The system is built with Python, Tkinter, and spaCy, with a simple in-app chat interface that mimics a basic conversational flow.

---

## Overview

The goal of Rapid-Health is to give users immediate, structured guidance when describing symptoms. Instead of scrolling through unreliable web results, users can type their symptoms naturally while the system interprets them, compares them with predefined medical profiles, and suggests likely conditions along with initial recommendations.

This project is not intended to replace professional medical advice. Rather, it acts as a first-level assistant before a user connects with a real doctor.

---

## Key Features

* **Conversational User Interface**
  A Tkinter-based chat window simulates a simple message-style interaction.

* **Symptom Understanding Using NLP**
  spaCy’s `en_core_web_md` model is used to compute similarity between user-entered symptom descriptions and known condition symptom sets.

* **Automated Condition Matching**
  Conditions are stored in a dictionary with symptom profiles and recommended actions. The system computes semantic similarity and returns the best match.

* **Doctor Connect Option**
  After receiving a preliminary assessment, the user can choose to exit or connect to a doctor.

* **Lightweight and Offline-Friendly**
  All logic runs locally without remote API calls.

---

## Tech Stack

* **Language:** Python 3
* **UI Framework:** Tkinter
* **NLP Library:** spaCy (`en_core_web_md`)
* **Similarity Model:** Word vector semantic similarity
* **Other:** Time module, basic Tkinter canvas and message formatting

---

## How to Run the Project

1. Install dependencies:

   ```bash
   pip install spacy
   python -m spacy download en_core_web_md
   ```

2. Make sure Tkinter is installed (it comes by default with most Python distributions).

3. Run the application:

   ```bash
   python Rapid_Health.py
   ```

The chat window will open automatically.

---

## Internal Logic and Architecture (Based on Code)

### 1. **Initialization**

The main class `HcB` loads the NLP model:

```python
self.n = spacy.load("en_core_web_md")
```

This provides vector embeddings used to compare user input with predefined symptoms. 

A dictionary `self.d` contains conditions, symptoms, and recommended actions.

### 2. **Chat State Machine**

The chatbot uses state variables such as:

* `self.st` → current conversation state
* `self.k` → the current data key being collected (age, weight, symptoms, etc.)
* `self.u` → stores user-provided details

Different states guide the conversation steps: greeting, collecting user info, asking for symptoms, and generating diagnosis.

### 3. **Symptom Similarity Logic**

When the user enters symptoms, the following logic executes:

```python
d1 = self.n(t)  # user input
for kk, vv in self.d.items():
    d2 = self.n(vv["s"])  # stored symptoms for each disease
    s = d1.similarity(d2)
```

* The system compares the input vector (`d1`) with each condition’s symptom vector (`d2`).
* It tracks the highest similarity score.
* If the score exceeds **0.45**, the condition is considered a match. Otherwise, the bot replies with a fallback message.

This method is simple but effective for small-scale medical triage.

### 4. **UI Rendering**

All messages (user and bot) are rendered on a Tkinter canvas using the `o()` method, which creates small chat bubbles. 

---

## Example Workflow

**User:** “I have been coughing a lot and my chest hurts when I breathe.”
**System:**

* Converts the sentence into a spaCy document
* Compares with stored symptom profiles (e.g., pneumonia, asthma)
* Suppose *pneumonia* has the highest similarity
* Similarity > 0.45 → considered a valid prediction

**Bot Output:**
“Looks like Pneumonia. Use antibiotics if needed and rest.”

---

## Accuracy Discussion

The system uses **vector similarity**, which is effective for general text but has limitations:

### Strengths:

* Understands natural phrasing
* Handles varied user descriptions
* Requires no advanced rule-based design

### Weaknesses:

* The dataset is small (10 conditions only)
* spaCy similarity is not medically precise
* It does not consider severity, duration, or multiple symptoms in detail
* May misclassify closely related illnesses
* No advanced ML model or probabilistic scoring

**Expected Accuracy:**
For generic, commonly described symptoms, accuracy is moderate.
For rare or complex phrasing, accuracy decreases.

---

## Future Scope

* Replace similarity-based detection with a **trained medical classifier** (transformers or fine-tuned BERT).
* Expand the symptom–disease database significantly.
* Add multi-symptom weighted scoring.
* Use a structured symptom ontology like SNOMED.
* Implement real chat-history context handling.
* Build a dedicated API layer and modern frontend (React, Flutter).
* Add user health profile tracking and analytics.
* Integrate an e-pharmacy and appointment booking system.

---

## Conclusion

Rapid-Health (QuickMed) is a lightweight, local, and beginner-friendly prototype for AI-assisted health triage. While not a substitute for medical professionals, it demonstrates how natural-language understanding and basic similarity scoring can be combined to deliver useful preliminary guidance.

