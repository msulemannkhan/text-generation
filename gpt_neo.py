from transformers import pipeline
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
      generator = pipeline('text-generation', model ='EleutherAI/gpt-neo-125M')
      post = sys.argv[1]
      result = generator(post, max_length=50, do_sample=True, temperature=0.9)
      print(result[0]['generated_text'])
