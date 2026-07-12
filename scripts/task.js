const fs = require("fs");

console.log("================================");
console.log("📋 Current Task");
console.log("================================\n");

if (!fs.existsSync("START_HERE.md")) {
  console.log("START_HERE.md not found.");
  process.exit(1);
}

console.log(fs.readFileSync("START_HERE.md", "utf8"));