const { execSync } = require("child_process");

console.log("================================");
console.log("🚀 PFL Engineering Workspace");
console.log("================================\n");

try {
  console.log("📂 Git Status");
  console.log(execSync("git status", { encoding: "utf8" }));
} catch (err) {
  console.log("Git not available.");
}

console.log("📌 Open these files first:");
console.log("- START_HERE.md");
console.log("- README.md");

console.log("\nToday's question:");
console.log("What is today's objective?");