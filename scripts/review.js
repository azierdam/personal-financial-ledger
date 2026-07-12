const { execSync } = require("child_process");

console.log("================================");
console.log("🔍 Engineering Review");
console.log("================================\n");

try {
    console.log(execSync("git status", { encoding: "utf8" }));
} catch {}

console.log("Checklist");

const checklist = [
    "README updated?",
    "START_HERE updated?",
    "Automation works?",
    "No unnecessary files?",
    "Ready to commit?"
];

checklist.forEach(item => console.log(`☐ ${item}`));