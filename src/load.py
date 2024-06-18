import requests

def fetch_text_from_url(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
url = "https://gutenberg.org/ebooks/84.txt.utf-8"  # Replace with your actual text file URL
content = fetch_text_from_url(url)

# content = content[3000:4000]


if content:
    print("Content:")
    # print(content)
else:
    print("Failed to fetch content.")
# print("------------------------------")


content = content.lower()
content = content.replace("\r\n", " ")
# print(content)
# print("------------------------------")

import nltk
nltk.download('punkt')  # Download the Punkt tokenizer models if not already downloaded

from nltk.tokenize import sent_tokenize




sentences = sent_tokenize(content)
with open("/veld/output/out.txt", "w") as f:
    for line_nr, sentence in enumerate(sentences):
        if line_nr > 6 and line_nr < 3080:
            f.write(sentence + "\n")

