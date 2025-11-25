# STATEMENT.md
## Project Statement — Rapid-Health (QuickMed)

Rapid-Health (QuickMed) is a lightweight NLP-based symptom assistant. It interprets user symptoms using spaCy’s `en_core_web_md` model and compares them with a small set of predefined medical conditions. It provides a probable match and basic guidance, but it is not a diagnostic tool.

### Objective
- Understand natural-language symptom descriptions  
- Match them to predefined condition profiles  
- Provide a quick preliminary suggestion  
- Recommend seeing a doctor when uncertain  

### Method
1. User inputs symptoms through a Tkinter chat interface.  
2. spaCy converts text into embeddings.  
3. Similarity scores determine the closest condition.  
4. If similarity is low, the system advises consulting a doctor.

### Scope & Limitations
- Limited condition list  
- Accuracy depends purely on text similarity  
- Not suitable for emergencies or clinical diagnosis  

### Future Scope
- Expanded medical dataset  
- ML-based prediction models  
- Improved UI and backend  
- Integration with e‑pharmacy and health tracking
