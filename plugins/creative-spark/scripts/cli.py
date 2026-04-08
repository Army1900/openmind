"""
Deep Sleep Dream Generator - CLI

Command-line interface for generating dream narratives from conversations.
"""

import argparse
import json
import sys
from pathlib import Path

from .extractor import FragmentExtractor
from .dream_engine import DreamEngine


def main():
    parser = argparse.ArgumentParser(
        description="Generate surreal dream narratives from conversation history"
    )
    parser.add_argument(
        '--context', '-c',
        type=str,
        help='Path to conversation JSON file',
        default=None
    )
    parser.add_argument(
        '--text', '-t',
        type=str,
        help='Raw conversation text',
        default=None
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output file path',
        default='deep-sleep-dream.md'
    )
    parser.add_argument(
        '--pairs', '-p',
        type=int,
        help='Number of dream pairs to generate',
        default=5
    )
    parser.add_argument(
        '--randomness', '-r',
        type=float,
        help='Randomness level (0-1, higher = more surreal)',
        default=0.3
    )
    parser.add_argument(
        '--format', '-f',
        type=str,
        choices=['json', 'prompt'],
        help='Output format: json (for LLM) or prompt (ready for LLM)',
        default='prompt'
    )

    args = parser.parse_args()

    # Get conversation text
    if args.context:
        with open(args.context, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Handle different conversation formats
            if isinstance(data, list):
                conversation = '\n\n'.join(
                    msg.get('content', str(msg)) for msg in data
                )
            else:
                conversation = data.get('conversation', str(data))
    elif args.text:
        conversation = args.text
    else:
        # Read from stdin
        conversation = sys.stdin.read()

    if not conversation or len(conversation.strip()) < 100:
        print("Error: Conversation text too short or empty", file=sys.stderr)
        sys.exit(1)

    # Extract fragments
    print("🔍 Extracting fragments...", file=sys.stderr)
    extractor = FragmentExtractor()
    fragments = extractor.extract(conversation)

    if len(fragments) < 2:
        print("Error: Not enough fragments to generate dream", file=sys.stderr)
        sys.exit(1)

    print(f"   Found {len(fragments)} fragments", file=sys.stderr)

    # Generate dream sequence
    print("💭 Generating dream sequence...", file=sys.stderr)
    engine = DreamEngine(randomness=args.randomness)
    dream_pairs = engine.generate_dream_sequence(fragments, num_pairs=args.pairs)

    if not dream_pairs:
        print("Error: Failed to generate dream sequence", file=sys.stderr)
        sys.exit(1)

    print(f"   Created {len(dream_pairs)} dream pairs", file=sys.stderr)

    # Output
    output_path = Path(args.output)

    if args.format == 'json':
        # Raw JSON for programmatic use
        result = engine.format_for_llm(dream_pairs)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result)
    else:
        # Prompt ready for LLM
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Dream Generator Output\n\n")
            f.write("```json\n")
            f.write(engine.format_for_llm(dream_pairs))
            f.write("\n```\n\n")
            f.write("---\n\n")
            f.write("**LLM Task:**\n\n")
            f.write("Using the dream pairs above, write a first-person surreal ")
            f.write("dream narrative. Use dream logic - metaphor, juxtaposition, ")
            f.write("time distortion. End with a '梦醒时分' section extracting ")
            f.write("2-3 key insights.\n")

    print(f"✅ Dream output written to: {output_path}", file=sys.stderr)

    # Print summary
    print(f"\n📊 Dream Summary:", file=sys.stderr)
    for i, pair in enumerate(dream_pairs, 1):
        print(f"   {i}. Opposition: {pair.opposition_score:.2f} | "
              f"'{pair.fragment_a.keywords[0] if pair.fragment_a.keywords else '...'}' "
              f"vs "
              f"'{pair.fragment_b.keywords[0] if pair.fragment_b.keywords else '...'}'",
              file=sys.stderr)


if __name__ == '__main__':
    main()
