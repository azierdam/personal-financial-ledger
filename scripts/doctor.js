const fs = require("fs");
const { execSync } = require("child_process");

console.log("================================");
console.log("🩺 PFL Doctor");
console.log("================================\n");

const files = [
  "README.md",
  "START_HERE.md",
  "package.json"
];

console.log("📁 Required Files");
files.forEach(file => {
  console.log(
    fs.existsSync(file)
      ? `✅ ${file}`
      : `❌ ${file}`
  );
});

console.log("\n🌿 Git");

try {
  console.log(execSync("git branch --show-current", {
    encoding: "utf8"
  }).trim());
} catch {
  console.log("❌ Git not available");
}

function check(command, name) {
  try {
    execSync(command, {
      stdio: "ignore"
    });
    console.log(`✅ ${name}`);
  } catch {
    console.log(`❌ ${name}`);
  }
}

console.log("\n🧰 Engineering Tools");

check("git --version", "Git");
check("node --version", "Node.js");
check("npm.cmd -v", "npm");
check("gemini --version", "Gemini CLI");
check("codex.cmd --version", "Codex CLI");

console.log("\n✅ Doctor completed.");