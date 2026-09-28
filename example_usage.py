from client import BPETokenizerEngine

def main():
    bpe = BPETokenizerEngine(vocab_size=15)
    corpus = "low lower newest widest lowest newer"
    stats = bpe.train(corpus)
    tokens = bpe.encode("lowest")
    print("BPE Tokenizer Verification:")
    print(f"Merges Learned: {stats['merges_learned']}")
    print(f"Encoded 'lowest': {tokens}")

if __name__ == "__main__":
    main()
