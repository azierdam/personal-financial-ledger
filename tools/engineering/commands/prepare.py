import sys
from . import doctor, context, prompt
from ..core import output

def run(agent):
    # 1. Doctor
    try:
        doctor.run()
    except SystemExit as e:
        if e.code != 0:
            sys.exit(e.code)
    except Exception as e:
        output.error(f"Doctor failed: {e}")
        sys.exit(1)

    # 2. Context
    try:
        context.run()
    except SystemExit as e:
        if e.code != 0:
            sys.exit(e.code)
    except Exception as e:
        output.error(f"Context generation failed: {e}")
        sys.exit(1)

    # 3. Prompt
    try:
        prompt.run(agent)
    except SystemExit as e:
        if e.code != 0:
            sys.exit(e.code)
    except Exception as e:
        output.error(f"Prompt generation failed: {e}")
        sys.exit(1)

    # Success summary
    print("\n✓ Doctor passed")
    print("✓ Context generated (.context.md)")
    print("✓ Prompt generated (.prompt.md)\n")
    print("Engineering preparation complete.")
