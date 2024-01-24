from datasets import load_dataset

# To load only a specific subset, pass it as an argument, e.g
ds_arxiv = load_dataset("EleutherAI/proof-pile-2", "algebraic-stack")
