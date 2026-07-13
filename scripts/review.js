const { execSync } = require("child_process");

console.log("================================");
console.log("🔍 Engineering Review");
console.log("================================\n");

try {
    console.log(execSync("git status", { encoding: "utf8" }));
} catch {}

const status = execSync("git status --short", {
    encoding: "utf8"
}).trim();

const lines = status ? status.split("\n") : [];

console.log(`📄 Files Changed : ${lines.length}`);

if (lines.length === 0) {
    console.log("\n🚦 Status");
    console.log("✅ Ready to commit");
} else {
    console.log("\n🚦 Status");
    console.log("⚠ Repository has pending changes");

    console.log("\nRecommendation");

    lines.forEach(line => {
        console.log(`• ${line}`);
    });
}