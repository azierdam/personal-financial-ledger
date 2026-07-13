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

console.log("\n📊 Repository Status");

if (!status) {
  console.log("✅ Working tree clean");

  console.log("\n💡 Recommendation");
  console.log("Repository is synchronized.");
} else {

  console.log(`⚠ ${status.split("\n").length} pending change(s)`);

  console.log("\n📝 Local Changes");
  console.log(status);

  console.log("\n💡 Recommendation");
  console.log("Commit or stash local changes before pulling.");
}

console.log("\n✅ Sync completed.");