# genpark-bpe-tokenizer-byte-pair-encoder-skill

> Byte-Pair Encoding (BPE) subword tokenizer trainer and deterministic text encoder/decoder.

Part of the **GenPark AI Agent Skills Matrix**. Production-ready, zero external dependencies, native Python 3.9+ standard library.

## Architecture

```mermaid
flowchart TD
    A[Text Input Corpus] --> B[Tokenization & Subword Extraction]
    B --> C[Vector & Similarity Kernels]
    C --> D[Ranked / Segmented Output]
    D --> E[MCP Protocol Endpoint]
```

## Features
- **Zero Third-Party Dependencies**: Pure Python standard library (`collections`, `re`, `math`).
- **High-Performance NLP**: Subword BPE merges, Okapi BM25 ranking, and Damerau-Levenshtein metrics.
- **Native MCP Protocol Support**: Integrated JSON-RPC 2.0 stdio server ready for Claude Desktop, Cursor, and Windsurf.

## Installation

```bash
pip install genpark-bpe-tokenizer-byte-pair-encoder-skill
```

Or clone directly:

```bash
git clone https://github.com/alphaparkinc/genpark-bpe-tokenizer-byte-pair-encoder-skill.git
cd genpark-bpe-tokenizer-byte-pair-encoder-skill
python example_usage.py
```

## Quick Start

```python
from client import *
# Refer to example_usage.py for end-to-end execution
```

## Model Context Protocol (MCP) Setup

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-bpe-tokenizer-byte-pair-encoder-skill": {
      "command": "python",
      "args": ["-m", "genpark-bpe-tokenizer-byte-pair-encoder-skill.mcp_server"]
    }
  }
}
```

## License
MIT License. Copyright (c) 2026 AlphaPark Inc. & Alpha-Park.
