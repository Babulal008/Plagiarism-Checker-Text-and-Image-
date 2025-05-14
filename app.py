import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import imagehash
import csv

# --------------- TEXT COMPARISON SECTION ---------------

def get_text_files():
    return [file for file in os.listdir() if file.endswith('.txt')]

def read_text_files(files):
    return [open(file, encoding='utf-8').read() for file in files]

# Use n-grams (bigrams or trigrams) and stopwords removal
def vectorize(texts, ngram_range=(1, 1)):
    return TfidfVectorizer(stop_words='english', ngram_range=ngram_range).fit_transform(texts).toarray()

def similarity(doc1, doc2):
    return cosine_similarity([doc1], [doc2])[0][0]

def check_text_plagiarism(files, vectors, similarity_threshold=0.8):
    results = set()
    paired_vectors = list(zip(files, vectors))
    for i in range(len(paired_vectors)):
        for j in range(i + 1, len(paired_vectors)):
            file1, vec1 = paired_vectors[i]
            file2, vec2 = paired_vectors[j]
            score = similarity(vec1, vec2)
            if score >= similarity_threshold:  # Apply threshold
                results.add((file1, file2, round(score, 4)))
    return results

# --------------- IMAGE COMPARISON SECTION ---------------

def get_image_files():
    return [file for file in os.listdir() if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

def resize_image(image, size=(256, 256)):
    return image.resize(size)

def get_image_hashes(files):
    image_hashes = {}
    for file in files:
        with Image.open(file) as img:
            img_resized = resize_image(img)  # Resize images before hashing
            image_hashes[file] = imagehash.phash(img_resized)
    return image_hashes

def compare_images(image_hashes):
    results = set()
    files = list(image_hashes.items())
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1, hash1 = files[i]
            file2, hash2 = files[j]
            diff = hash1 - hash2  # Hamming distance
            results.add((file1, file2, diff))
    return results

# --------------- EXPORT RESULTS TO CSV ---------------

def export_results_to_csv(results, file_name="plagiarism_results.csv"):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["File1", "File2", "Similarity/Difference"])
        for res in results:
            writer.writerow(res)

# --------------- RUN EVERYTHING ---------------

def main():
    print("Checking text files...")
    text_files = get_text_files()
    if text_files:
        texts = read_text_files(text_files)
        vectors = vectorize(texts, ngram_range=(1, 2))  # Using bigrams for better context
        text_results = check_text_plagiarism(text_files, vectors, similarity_threshold=0.85)  # Threshold of 85%
        for res in sorted(text_results, key=lambda x: x[2], reverse=True):
            print(f"[TEXT] Similarity between {res[0]} and {res[1]}: {res[2]*100:.2f}%")
        export_results_to_csv(text_results, "text_plagiarism_results.csv")
    else:
        print("No text files found.")

    print("\nChecking image files...")
    image_files = get_image_files()
    if image_files:
        image_hashes = get_image_hashes(image_files)
        image_results = compare_images(image_hashes)
        for res in sorted(image_results, key=lambda x: x[2]):
            print(f"[IMAGE] Difference between {res[0]} and {res[1]}: {res[2]} (0 means identical)")
        export_results_to_csv(image_results, "image_plagiarism_results.csv")
    else:
        print("No image files found.")

if __name__ == "__main__":
    main()
