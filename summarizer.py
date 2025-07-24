import openai
import os

# Set your OpenAI API key here
openai.api_key = "sk-..."  # ← replace this with your real key

def summarize_text(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Summarize the following:\n\n{text}"}
            ],
            temperature=0.5,
            max_tokens=300
        )
        summary = response['choices'][0]['message']['content']
        return summary.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("📄 AI Text Summarizer\n")
    input_text = input("Paste the text you want to summarize:\n\n")
    print("\nSummarizing...\n")
    result = summarize_text(input_text)
    print("🧠 Summary:\n", result)
