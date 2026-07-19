# tools/engineering/__main__.py
import argparse
import sys
from .commands import doctor, context, prompt

def main():
    parser = argparse.ArgumentParser(description="Engineering CLI for PFL")
    subparsers = parser.add_subparsers(dest="command")

    # doctor
    subparsers.add_parser("doctor", help="Validate repository environment")

    # context
    subparsers.add_parser("context", help="Generate repository context")

    # prompt
    prompt_parser = subparsers.add_parser("prompt", help="Generate engineering prompt")
    prompt_parser.add_argument("agent", choices=["gemini"], help="Target AI agent")

    args = parser.parse_args()

    if args.command == "doctor":
        doctor.run()
    elif args.command == "context":
        context.run()
    elif args.command == "prompt":
        prompt.run(args.agent)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
