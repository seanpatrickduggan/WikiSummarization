## Table of Contents

- [Wikipedia Page Summarizer](#wikipedia-page-summarizer)
- [Coming Soon](#coming-soon)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
  1. [Clone or Download the Repository](#1-clone-or-download-the-repository)
  2. [Create a Virtual Environment (Optional but Recommended)](#2-create-a-virtual-environment-optional-but-recommended)
  3. [Install Dependencies](#3-install-dependencies)
  4. [Run the Script](#4-run-the-script)
  5. [View the Results](#5-view-the-results)
- [License](#license)

# Wikipedia Page Summarizer

This Python script allows you to fetch and summarize content from Wikipedia articles using the Wikipedia API and the BERT Extractive Summarizer. It also saves the fetched text and the generated summary to separate text files.

Please be nice to wikipedia and me, as the code uses their free API, and an agent with my email specified. If you want to run the code, please modify it with your own information in the custom user agent variable.

Currently the topic is hard-coded to be "Dog".

# Coming Soon
- More organized output, possibly a database for storing pages and summaries
- Options to choose between summarization models
- Exploring the Wikipedia API for 
  - A "parseable" output, e.g. sections, subsections, references, etc.
  - Search functionality, checking if a similar page exists, etc.
- Creating a UI for the script allowing for: 
    - Tracking/saving summaries
    - Summarizing using a different model


### Prerequisites
Ensure that you have Python and pip installed on your system before creating the virtual environment and installing dependencies.

## Usage

1. **Clone or Download the Repository:**
- Clone or download this repository to your local machine:

```bash
git clone https://github.com/seanpatrickduggan/WikiSummarization.git
```

2. **Create a Virtual Environment (Optional but Recommended):**
- It's a good practice to create a virtual environment to isolate project dependencies. Open your terminal and navigate to the project directory:

```bash
cd WikiSummarization
```

- Create a virtual environment:

```bash
python -m venv venv
```

- Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS and Linux:
```bash
source venv/bin/activate
```

3. **Install Dependencies:**
- With the virtual environment activated, install the required Python libraries from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install the necessary libraries, including Wikipedia-API, BERT Extractive Summarizer, and Torch.

4. **Run the Script:**
- Modify the `topic` variable in the `main` function of `WikiSummarization.py` to specify the Wikipedia topic you want to summarize.
- Run the script:

```bash
python WikiSummarization.py
```

5. **View the Results:**
- The script will fetch the Wikipedia page for the specified topic, extract the text content, and save it to a file named `text.txt`. It will then use the BERT Extractive Summarizer to generate a summary and save it to a file named `summary.txt`.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE). For more details, see the [LICENSE](LICENSE) file.
