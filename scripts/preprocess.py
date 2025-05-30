import argparse
import logging
import sys
from sacremoses import MosesTokenizer


def parse_args():
    parser = argparse.ArgumentParser(
        description="Tokenize source and target files using Moses tokenizer."
    )
    parser.add_argument(
        "--src", type=str, required=True,
        help="Path to source language file (raw)."
    )
    parser.add_argument(
        "--tgt", type=str, required=True,
        help="Path to target language file (raw)."
    )
    parser.add_argument(
        "--output-src", type=str, required=True,
        help="Path to write tokenized source file."
    )
    parser.add_argument(
        "--output-tgt", type=str, required=True,
        help="Path to write tokenized target file."
    )
    parser.add_argument(
        "--src-lang", type=str, default="it",
        help="Language code for source (Sacremoses)."
    )
    parser.add_argument(
        "--tgt-lang", type=str, default="en",
        help="Language code for target (Sacremoses)."
    )
    return parser.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(level=logging.INFO)

    try:
        with open(args.src, encoding="utf-8") as f_src:
            src_lines = f_src.read().splitlines()
        with open(args.tgt, encoding="utf-8") as f_tgt:
            tgt_lines = f_tgt.read().splitlines()
    except IOError as e:
        logging.error(f"Failed to read input files: {e}")
        sys.exit(1)

    if len(src_lines) != len(tgt_lines):
        logging.error(
            f"Line count mismatch: source has {len(src_lines)}, target has {len(tgt_lines)}"
        )
        sys.exit(1)
    logging.info(f"Tokenizing {len(src_lines)} sentence pairs.")

    src_tok = MosesTokenizer(lang=args.src_lang)
    tgt_tok = MosesTokenizer(lang=args.tgt_lang)

    try:
        with open(args.output_src, 'w', encoding="utf-8") as out_src, \
             open(args.output_tgt, 'w', encoding="utf-8") as out_tgt:
            for src_line, tgt_line in zip(src_lines, tgt_lines):
                tok_src = src_tok.tokenize(src_line, escape=False)
                tok_tgt = tgt_tok.tokenize(tgt_line, escape=False)
                out_src.write(" ".join(tok_src) + "\n")
                out_tgt.write(" ".join(tok_tgt) + "\n")
    except IOError as e:
        logging.error(f"Failed to write output files: {e}")
        sys.exit(1)

    logging.info("Tokenization complete.")


if __name__ == '__main__':
    main()
