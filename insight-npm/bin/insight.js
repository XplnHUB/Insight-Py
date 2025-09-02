#!/usr/bin/env node
const { spawn } = require("child_process");
const path = require("path");

const pythonCmd = process.platform === "win32" ? "python" : "python3";
const cliPath = path.resolve(__dirname, "../../insight/cli.py");


const args = process.argv.slice(2);

const proc = spawn(pythonCmd, [cliPath, ...args], { stdio: "inherit" });

proc.on("close", (code) => {
  process.exit(code);
});
