# tools/engineering/__main__.py
import argparse
import sys
from .commands import doctor, context, prompt, prepare, package

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

    # prepare
    prepare_parser = subparsers.add_parser("prepare", help="Orchestrate doctor, context, and prompt commands")
    prepare_parser.add_argument("agent", choices=["gemini"], help="Target AI agent")
    
    # package
    package_parser = subparsers.add_parser("package", help="Package review artifacts")
    package_parser.add_argument("profile", choices=["chatgpt"], help="Packaging profile")

    args = parser.parse_args()

    if args.command == "doctor":
        doctor.run()
    elif args.command == "context":
        context.run()
    elif args.command == "prompt":
        prompt.run(args.agent)
    elif args.command == "prepare":
        prepare.run(args.agent)
    elif args.command == "package":
        package.run(args.profile)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
