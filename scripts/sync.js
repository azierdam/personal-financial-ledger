const { execSync } = require("child_process");

console.log("================================");
console.log("🔄 PFL Sync");
console.log("================================\n");

function run(cmd) {
  try {
    return execSync(cmd, {
      encoding: "utf8",
      stdio: "pipe"
    }).trim();
  } catch (err) {
    return null;
  }
}

const branch = run("git branch --show-current");
const status = run("git status --short");

console.log(`🌿 Branch : ${branch}`);

if (!status) {
  console.log("✅ Working tree clean");
} else {
  console.log("\n📝 Local Changes");
  console.log(status);
}

console.log("\n⬇ Pulling latest...");

const pull = run("git pull");

if (pull) {
  console.log(pull);
} else {
  console.log("❌ Pull failed");
}

console.log("\n✅ Sync completed.");