import os
import json
import shutil
from datetime import datetime

def execute_cleanup(root):
    findings_path = os.path.join(root, ".engineering", "findings", "approved-findings.json")
    with open(findings_path, 'r', encoding='utf-8') as f:
        findings = json.load(f)

    cleanup_log = []
    execution_results = []

    for finding in findings:
        action = finding['approved_action']
        finding_id = finding['finding_id']
        
        result = {"finding_id": finding_id, "approved_action": action, "affected_files": [], "result": "Success", "reason": ""}
        
        try:
            if action == "Relocate" and finding_id == "FIND-ORG-001":
                src = os.path.join(root, "archive", "planning-artifacts")
                dst = os.path.join(root, "archive", "planning")
                shutil.move(src, dst)
                result["affected_files"] = [src, dst]
            elif action == "Archive" and finding_id == "FIND-DUP-001":
                os.makedirs(os.path.join(root, "archive", "obsolete"), exist_ok=True)
                src = os.path.join(root, "archive", "README.md")
                dst = os.path.join(root, "archive", "obsolete", "README-archive.md")
                shutil.move(src, dst)
                result["affected_files"] = [src, dst]
            else:
                result["result"] = "Skipped"
                result["reason"] = "Action not implemented in this version"
        except Exception as e:
            result["result"] = "Failed"
            result["reason"] = str(e)
            
        execution_results.append(result)
        cleanup_log.append(f"{datetime.now().isoformat()} - {finding_id}: {action} - {result['result']}")

    # Save outputs
    output_dir = os.path.join(root, ".engineering", "cleanup")
    with open(os.path.join(output_dir, "cleanup-execution.json"), 'w', encoding='utf-8') as f:
        json.dump(execution_results, f, indent=2, sort_keys=True)
    with open(os.path.join(output_dir, "cleanup-log.json"), 'w', encoding='utf-8') as f:
        json.dump(cleanup_log, f, indent=2, sort_keys=True)
    with open(os.path.join(output_dir, "cleanup-summary.md"), 'w', encoding='utf-8') as f:
        f.write("# Cleanup Summary\n\n")
        for res in execution_results:
            f.write(f"- {res['finding_id']}: {res['result']} ({res['reason'] if res['reason'] else 'No reason'})\n")
