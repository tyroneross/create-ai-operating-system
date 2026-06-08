#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const packageRoot = path.resolve(__dirname, "..");
const templatesRoot = path.join(packageRoot, "templates");
const sharedRoot = path.join(templatesRoot, "_shared");
const validTemplates = new Set(["work", "personal"]);

function usage() {
  console.log(`Usage: create-ai-operating-system <target-dir> [options]

Scaffold a local-first AI Operating System.

Options:
  --template <work|personal>  choose the generated template (default: personal)
  --work                      shortcut for --template work
  --personal                  shortcut for --template personal
  --force                     overwrite an existing non-empty target directory
  --help                      show this help message`);
}

function fail(message) {
  console.error(`error: ${message}`);
  process.exit(1);
}

function parseArgs(argv) {
  let template = "personal";
  let force = false;
  const positional = [];

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--help" || arg === "-h") {
      usage();
      process.exit(0);
    }
    if (arg === "--force") {
      force = true;
      continue;
    }
    if (arg === "--work") {
      template = "work";
      continue;
    }
    if (arg === "--personal") {
      template = "personal";
      continue;
    }
    if (arg === "--template") {
      const value = argv[i + 1];
      if (!value) {
        fail("--template requires work or personal");
      }
      template = value;
      i += 1;
      continue;
    }
    if (arg.startsWith("--template=")) {
      template = arg.slice("--template=".length);
      continue;
    }
    if (arg.startsWith("--")) {
      fail(`unknown option ${arg}`);
    }
    positional.push(arg);
  }

  if (!validTemplates.has(template)) {
    fail(`unknown template ${template}; expected work or personal`);
  }
  if (positional.length !== 1) {
    usage();
    process.exit(positional.length === 0 ? 0 : 1);
  }
  return { targetDir: positional[0], template, force };
}

function isEmptyDir(dir) {
  if (!fs.existsSync(dir)) {
    return true;
  }
  const stat = fs.statSync(dir);
  if (!stat.isDirectory()) {
    fail(`target exists and is not a directory: ${dir}`);
  }
  return fs.readdirSync(dir).length === 0;
}

function assertSafeRemovalTarget(dir) {
  const parsed = path.parse(dir);
  if (dir === parsed.root) {
    fail("refusing to remove filesystem root");
  }
  if (dir === process.cwd()) {
    fail("refusing to remove the current working directory");
  }
  if (dir === packageRoot) {
    fail("refusing to remove the package root");
  }
}

function shouldSkip(entry) {
  return [".DS_Store", "__pycache__", ".pytest_cache"].includes(entry.name);
}

function copyTemplate(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    if (shouldSkip(entry)) {
      continue;
    }
    const srcPath = path.join(src, entry.name);
    const destName = entry.name === "gitignore" ? ".gitignore" : entry.name;
    const destPath = path.join(dest, destName);
    if (entry.isDirectory()) {
      copyTemplate(srcPath, destPath);
    } else if (entry.isSymbolicLink()) {
      fs.symlinkSync(fs.readlinkSync(srcPath), destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
      fs.chmodSync(destPath, fs.statSync(srcPath).mode);
    }
  }
}

function main() {
  const { targetDir, template, force } = parseArgs(process.argv.slice(2));
  const variantRoot = path.join(templatesRoot, template);

  for (const requiredPath of [sharedRoot, variantRoot]) {
    if (!fs.existsSync(requiredPath)) {
      fail(`template directory not found: ${requiredPath}`);
    }
  }

  const resolvedTarget = path.resolve(process.cwd(), targetDir);
  const targetIsEmpty = isEmptyDir(resolvedTarget);
  if (!targetIsEmpty && !force) {
    fail(`target directory is not empty: ${resolvedTarget}. Re-run with --force to overwrite.`);
  }
  if (!targetIsEmpty && force) {
    assertSafeRemovalTarget(resolvedTarget);
    fs.rmSync(resolvedTarget, { recursive: true, force: true });
  }

  fs.mkdirSync(resolvedTarget, { recursive: true });
  copyTemplate(sharedRoot, resolvedTarget);
  copyTemplate(variantRoot, resolvedTarget);

  const displayTarget = path.isAbsolute(targetDir) ? resolvedTarget : targetDir;
  console.log(`Created ${template} AI Operating System at ${displayTarget}`);
  console.log("");
  console.log("Next steps:");
  console.log(`  cd ${JSON.stringify(displayTarget)}`);
  console.log("  python3 tools/scripts/wiki_index.py rebuild");
  console.log("  ./tools/scripts/llmwiki status");
}

main();
