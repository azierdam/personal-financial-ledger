const fs = require("fs");

console.log("================================");
console.log("📋 Current Task");
console.log("================================\n");

if (!fs.existsSync("START_HERE.md")) {
  console.log("START_HERE.md not found.");
  process.exit(1);
}

const text = fs.readFileSync("START_HERE.md", "utf8");

const sections = [
  "## Current Phase",
  "## Current Sprint",
  "## Current Task",
  "## Next Task",
  "## Weekend Queue"
];

for (const section of sections) {
  const start = text.indexOf(section);

  if (start === -1) continue;

  const next = text.indexOf("\n## ", start + 1);

  console.log(
    text.substring(
      start,
      next === -1 ? text.length : next
    ).trim()
  );

  console.log("");
}