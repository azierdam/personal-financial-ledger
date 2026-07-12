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
  console.log(execSync("git branch --show-current", { encoding: "utf8" }).trim());
} catch {
  console.log("❌ Git not available");
}

console.log("\n📦 Node");

console.log(process.version);

console.log("\n✅ Doctor completed.");