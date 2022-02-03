import transformers
import streamlit as st

from transformers import AutoTokenizer, AutoModelWithLMHead
  
tokenizer = AutoTokenizer.from_pretrained("gpt2-large")
@st.cache
def load_model(model_name):
    model = AutoModelWithLMHead.from_pretrained("gpt2-large")
    return model

model = load_model("gpt2-large")

def infer(input_ids, max_length, temperature, top_k, top_p):

    output_sequences = model.generate(
        input_ids=input_ids,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        do_sample=True,
        num_return_sequences=1
    )

    return output_sequences
default_value = "See how a modern neural network auto-completes your text 🤗 This site, built by the Hugging Face team, lets you write a whole document directly from your browser, and you can trigger the Transformer anywhere using the Tab key. Its like having a smart machine that completes your thoughts 😀 Get started by typing a custom snippet, check out the repository, or try one of the examples. Have fun!"

#prompts
st.title("Write with Transformers 🦄")
st.write("The almighty king of text generation, GPT-2 comes in four available sizes, only three of which have been publicly made available. Feared for its fake news generation capabilities, it currently stands as the most syntactically coherent model. A direct successor to the original GPT, it reinforces the already established pre-training/fine-tuning killer duo. From the paper: Language Models are Unsupervised Multitask Learners by Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei and Ilya Sutskever.")

sent = st.text_area("Text", default_value, height = 275)
max_length = st.sidebar.slider("Max Length", min_value = 10, max_value=30)
temperature = st.sidebar.slider("Temperature", value = 1.0, min_value = 0.0, max_value=1.0, step=0.05)
top_k = st.sidebar.slider("Top-k", min_value = 0, max_value=5, value = 0)
top_p = st.sidebar.slider("Top-p", min_value = 0.0, max_value=1.0, step = 0.05, value = 0.9)

encoded_prompt = tokenizer.encode(sent, add_special_tokens=False, return_tensors="pt")
if encoded_prompt.size()[-1] == 0:
    input_ids = None
else:
    input_ids = encoded_prompt


output_sequences = infer(input_ids, max_length, temperature, top_k, top_p)



for generated_sequence_idx, generated_sequence in enumerate(output_sequences):
    print(f"=== GENERATED SEQUENCE {generated_sequence_idx + 1} ===")
    generated_sequences = generated_sequence.tolist()

    # Decode text
    text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)

    # Remove all text after the stop token
    #text = text[: text.find(args.stop_token) if args.stop_token else None]

    # Add the prompt at the beginning of the sequence. Remove the excess text that was used for pre-processing
    total_sequence = (
        sent + text[len(tokenizer.decode(encoded_prompt[0], clean_up_tokenization_spaces=True)) :]
    )

    generated_sequences.append(total_sequence)
    print(total_sequence)


st.write(generated_sequences[-1])
