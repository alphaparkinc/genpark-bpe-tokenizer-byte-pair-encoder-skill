"""Byte-Pair Encoding (BPE) Subword Tokenizer Engine
100% Python Standard Library (collections, re).
"""

import collections
import re

class BPETokenizerEngine:
    """Byte-Pair Encoding vocabulary learner and subword tokenizer."""
    def __init__(self, vocab_size=50):
        self.vocab_size = vocab_size
        self.merges = {}

    def _get_stats(self, vocab):
        pairs = collections.defaultdict(int)
        for word, freq in vocab.items():
            symbols = word.split()
            for i in range(len(symbols) - 1):
                pairs[(symbols[i], symbols[i + 1])] += freq
        return pairs

    def _merge_vocab(self, pair, v_in):
        v_out = {}
        bigram = " ".join(pair)
        replacement = "".join(pair)
        for word in v_in:
            w_out = word.replace(bigram, replacement)
            v_out[w_out] = v_in[word]
        return v_out

    def train(self, corpus):
        words = re.findall(r"\w+|\S", corpus.lower())
        vocab = collections.defaultdict(int)
        for w in words:
            vocab[" ".join(list(w)) + " </w>"] += 1

        self.merges = {}
        for i in range(self.vocab_size):
            pairs = self._get_stats(vocab)
            if not pairs:
                break
            best = max(pairs, key=pairs.get)
            vocab = self._merge_vocab(best, vocab)
            self.merges[best] = i

        return {
            "merges_learned": len(self.merges),
            "top_merges": [list(k) for k in list(self.merges.keys())[:5]]
        }

    def encode(self, text):
        words = re.findall(r"\w+|\S", text.lower())
        tokens = []
        for word in words:
            w_tokens = list(word) + ["</w>"]
            for pair in self.merges:
                bigram = "".join(pair)
                i = 0
                while i < len(w_tokens) - 1:
                    if w_tokens[i] == pair[0] and w_tokens[i + 1] == pair[1]:
                        w_tokens[i : i + 2] = [bigram]
                    else:
                        i += 1
            tokens.extend(w_tokens)
        return tokens
