from transformers import AutoTokenizer, AutoModelForCausalLM

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/llemma_7b")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/llemma_7b").cuda()

print("Enter a Lean theorem (end with a line containing 'END' or type 'exit' to quit):")
while True:
    lines = []
    while True:
        line = input()
        if line.lower() == 'exit':
            exit(0)
        if line == 'END':
            break
        lines.append(line)

    lean_theorem = '\n'.join(lines)
    if len(lean_theorem) == 0:
        # Skip empty input
        continue

    # Tokenize input
    inputs = tokenizer(lean_theorem, return_tensors="pt").to(model.device)

    # Generate output
    print("Generating output...")
    output = model.generate(**inputs, max_new_tokens=256)

    # Decode the output
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    print(decoded_output)

    print("\nEnter a Lean theorem (end with a line containing 'END' or type 'exit' to quit):")
