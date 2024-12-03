# openai-finetune-management
This project provides a script to manage OpenAI fine-tuned models. It includes functionalities to remove and list fine-tuned models using the OpenAI API.
## Prerequisites

- Python 3.x
- OpenAI Python client library

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/openai-finetune-management.git
   cd openai-finetune-management
   ```

2. **Install Required Packages**

   Install the OpenAI API client:

   ```bash
   pip install openai
   ```

3. **Set the OpenAI API Key**

   You'll need to set your OpenAI API key to the `main.py`. Replace `YOUR_API_KEY` with your actual API key.

     ```python
     os.environ["OPENAI_API_KEY"] = "your_api_key_here"
     ```

4. **Run the Script**

   Execute the script to manage fine-tuned models:

   ```bash
   python manage_models.py
   ```

## Script Functionalities

- **Remove Fine-Tuned Model**: Deletes specific fine-tuned models.
- **List Fine-Tuned Models**: Lists all remaining fine-tuned models.

## Contributions

Contributions to improve and enhance the script are welcome. Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
