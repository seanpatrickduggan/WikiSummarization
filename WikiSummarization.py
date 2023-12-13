import os
import wikipediaapi
import requests
from summarizer import Summarizer

def main():
    # Get user input for the topic
    topic = "Dog" # input("Enter a topic to summarize: ")
    print("Getting Wikipedia page for topic:", topic)
    
    # Define a custom user agent
    user_agent = "Wikipedia Example Scraper 1.0 (sean.duggan.cs@gmail.com)"
    print("User agent:", user_agent)
    
    # Initialize the Wikipedia API with the custom user agent
    print("Initializing Wikipedia API with user agent...")
    wiki_wiki = wikipediaapi.Wikipedia(user_agent, 'en')
    
    # Check if the text file already exists and has content
    text = ""
    if os.path.exists("text.txt") and os.path.getsize("text.txt") > 0:
        # Read the text file
        print("Reading text from file...")
        with open("text.txt", "r") as file:
            text = file.read()
        
    else:
        # Fetch the Wikipedia page for the given topic
        page = wiki_wiki.page(topic)

        # Check if the page exists and has content
        if page.exists() and page.text:
            # Extract the text content of the page
            print("Extracting text content from page...")
            text = page.text
            # Save the text to a file
            print("Saving text content to file...")
            with open("text.txt", "wb") as file:
                encoded_text = text.encode("utf-8", "ignore")
                file.write(encoded_text)
        else:
            print("Topic not found or does not have content on Wikipedia.")
            
    if text:
        # Initialize the BERT Extractive Summarizer
        print("Initializing BERT Extractive Summarizer...")
        summarizer = Summarizer()

        # Summarize the text using BERT Extractive Summarizer
        print("Summarizing text...")
        summarized_text = summarizer(text)

        # Print the summary
        print("\nSummary:")
        print(summarized_text)
        # Save the summary to a file
        print("Saving summary to file...")
        with open("summary.txt", "w") as file:
            file.write(summarized_text)
    else:
        print("No text to summarize.")

if __name__ == "__main__":
    main()