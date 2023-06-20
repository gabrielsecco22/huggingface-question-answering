## Question Answering from Company Documentation Corpus using Hugging Face Transformers

This repository contains code and resources for building a Question Answering (QA) system from a company documentation corpus using Hugging Face Transformers. The QA system utilizes powerful transformer models to extract precise information from a collection of company documents.

### Requirements
- Python 3.7 or above
- Hugging Face Transformers library
- Wikipedia API library (for the provided sample code)
- Other dependencies as listed in the `requirements.txt` file

### Installation
1. Clone this repository:
2. Navigate to the repository:
3. Install the required dependencies: `pip install -r requirements.txt`

### Usage
1. Change desired topics in the file as needed.
2. Run the `wikipedia_data_fech.py` script to collect data from Wikipedia. This script will create a `data` directory and save the data in .TXT files.
3. Run the `qa.py` script to use the QA system. The script will prompt you to enter a question. The script will then search for the answer in the document corpus and return the answer if found.

Please refer to the code and comments within the repository for more detailed instructions and guidance on each step.

### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

### License
This project is licensed under the [MIT License](LICENSE).

### Acknowledgments
- [Hugging Face Transformers](https://huggingface.co/transformers) - for providing the powerful transformer models and resources.
- [Wikipedia API](https://pypi.org/project/Wikipedia-API/) - for the sample code on data collection from Wikipedia.

### Disclaimer
This repository serves as a tutorial and starting point for building a QA system from a company documentation corpus. It is important to customize and adapt the code, data, and approaches to suit your specific use case and requirements. The provided code and resources are not intended to be used as-is for production environments, but rather as a learning resource.