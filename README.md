# Plagiarism Checker

**Plagiarism Checker** is a Python-based tool designed to detect similarities and potential plagiarism in both **text files** and **image files**. The tool uses advanced algorithms like **TF-IDF** (Term Frequency-Inverse Document Frequency) and **cosine similarity** for text comparison, and **Perceptual Hashing (pHash)** for image comparison.

- **Text Comparison**: Detects plagiarism in text files based on their content.
- **Image Comparison**: Detects near-identical or altered images using perceptual hashing.
- **CSV Export**: Saves the results of the plagiarism check in CSV format for further review and analysis.

![Plagiarism Checker](https://via.placeholder.com/1200x400.png?text=Plagiarism+Checker+Tool)

[Capture1](https://github.com/user-attachments/assets/a2bfd2b3-98c3-4ec6-a775-244bf8590094)
![Capture2](https://github.com/user-attachments/assets/75f62146-1e12-4511-99fd-0653d66ca297)
## Features!

### **Text Comparison**
- **TF-IDF** and **cosine similarity** are used to measure similarity between text files.
- Supports **N-grams** (e.g., bigrams or trigrams) to provide more context and improve the comparison.
- **Threshold** for similarity can be customized to only flag files with a certain level of similarity.

### **Image Comparison**
- Compares images using **Perceptual Hashing (pHash)**, which is robust to minor alterations such as resizing, cropping, and color adjustments.
- Calculates the **Hamming distance** to determine image similarity (a difference of 0 means the images are identical).
- Detects near-identical images, even with minor modifications.

### **CSV Export**
- Both text and image plagiarism results are saved in separate CSV files:
  - `text_plagiarism_results.csv`
  - `image_plagiarism_results.csv`

---

## Getting Started

Follow these steps to get the plagiarism checker up and running on your local machine.

### Prerequisites

Make sure you have the following installed on your system:
- **Python 3.x**
- **pip** (Python package manager)

### 1. Clone or Download the Repository

Clone the repository using Git:

```bash
git clone https://github.com/yourusername/plagiarism-checker.git
