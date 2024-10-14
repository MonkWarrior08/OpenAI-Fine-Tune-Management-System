import openai
import os

# Set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = ""

# Predefined list of fine-tuned models
fine_tuned_models = [
    ""
]

def remove_finetune_model(model_id):
    try:
        client = openai.OpenAI()  # The client will automatically use the environment variable
        client.models.delete(model_id)
        print(f"Successfully deleted fine-tuned model: {model_id}")
        return True
    except openai.OpenAIError as e:
        print(f"Error deleting fine-tuned model {model_id}: {e}")
        return False

def list_finetune_models():
    try:
        client = openai.OpenAI()
        models = client.models.list()
        return [model.id for model in models if model.id.startswith("ft:")]
    except openai.OpenAIError as e:
        print(f"Error listing models: {e}")
        return []

# Delete all models in the list
for model in fine_tuned_models:
    remove_finetune_model(model)

# List remaining fine-tuned models
print("\nRemaining fine-tuned models:")
remaining_models = list_finetune_models()
if remaining_models:
    for model in remaining_models:
        print(f"- {model}")
else:
    print("No fine-tuned models remaining.")
