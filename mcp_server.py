import sys
import json
from client import BPETokenizerEngine

tokenizer = BPETokenizerEngine(vocab_size=30)
# Pre-seed with default English vocabulary
tokenizer.train("the and of to in a is that for it as was with on at by this from they we say her she")

def handle_rpc(line):
    try:
        req = json.loads(line)
    except Exception:
        return
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "genpark-bpe-tokenizer-byte-pair-encoder-skill", "version": "1.0.0"},
            "capabilities": {"tools": {}}
        }
    elif method == "tools/list":
        res = {
            "tools": [
                {
                    "name": "train_and_encode",
                    "description": "Train BPE merges on corpus and encode input text into subwords",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "corpus": {"type": "string", "description": "Training corpus text"},
                            "text": {"type": "string", "description": "Text to tokenize"},
                            "vocab_size": {"type": "integer", "default": 25}
                        },
                        "required": ["text"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "train_and_encode":
            corpus = args.get("corpus")
            text = args.get("text", "")
            vs = args.get("vocab_size", 25)
            engine = BPETokenizerEngine(vocab_size=vs)
            if corpus:
                engine.train(corpus)
            else:
                engine.train(text)
            tokens = engine.encode(text)
            res = {"content": [{"type": "text", "text": json.dumps({"token_count": len(tokens), "tokens": tokens})}]}
        else:
            res = {"isError": True, "content": [{"type": "text", "text": f"Unknown tool {tool_name}"}]}
    else:
        res = {"error": {"code": -32601, "message": "Method not found"}}

    resp = {"jsonrpc": "2.0", "id": req_id, "result": res.get("result", res)}
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        if line.strip():
            handle_rpc(line.strip())

if __name__ == "__main__":
    main()
