# AI-powered YouTube Transcript Summarizer with MongoDB Atlas Vector Search

This repository contains a Python-based solution for summarizing YouTube video transcripts using OpenAI and storing the summarized data, along with embeddings, in MongoDB Atlas using its Vector Search feature.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Features

- Fetches YouTube video metadata and transcripts.
- Summarizes video content using OpenAI's GPT models.
- Converts summarized transcripts into embeddings for searchability.
- Stores video details, summaries, and embeddings in MongoDB Atlas with [Vector Search capability](https://www.mongodb.com/products/platform/atlas-vector-search).

## Prerequisites

- Python 3.8+
- MongoDB Atlas account
- OpenAI account

## Installation

1. **Clone the Repository**:
  ```bash
   git clone https://github.com/fabiofalavinha/mongodb-ai-video-transcript.git
   cd mongodb-ai-video-transcript
  ```
2. **Set Up a Virtual Environment**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

3. **Install Dependencies**:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. Configure the config.ini file with your OpenAI API key and MongoDB Atlas connection details.
2. Run the script:

```bash
  python main.py
  For searching within the stored embeddings in MongoDB Atlas:
```

```bash
  python search.py "your_search_query_here"
```

## Contributing

1. Fork the repository on GitHub.
2. Clone the forked repo to your machine.
3. Create a new branch in your local repo.
4. Make your changes and commit them to your local branch.
5. Push your local branch to your fork on GitHub.
6. Create a pull request from your fork to the original repository.

Please ensure that your code adheres to the repo's coding standards and include tests where necessary.

## Acknowledgments

Thanks to OpenAI for their powerful GPT models.
MongoDB team for the incredible Atlas Vector Search feature.
