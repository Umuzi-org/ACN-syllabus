const fs = require("fs");
const path = require("path");

function extractContentPaths(syllabusContent) {
  return syllabusContent.match(/path="(.*?)"/g).map(match => match.slice(6, -1));
}

function findOrphanNodes(contentDirectory, syllabusPaths) {
  const orphanNodes = [];

  const subdirectories = fs.readdirSync(contentDirectory, { withFileTypes: true })
    .filter(item => item.isDirectory())
    .map(item => item.name);

  for (const subdirectory of subdirectories) {
    const subdirectoryPath = path.join(contentDirectory, subdirectory);
    const hasInnerOrphans = findOrphanNodes(subdirectoryPath, syllabusPaths);

    if (!syllabusPaths.includes(subdirectory) && !hasInnerOrphans.length) {
      orphanNodes.push(subdirectoryPath);
    } else {
      orphanNodes.push(...hasInnerOrphans);
    }
  }

  return orphanNodes;
}

const contentDirectory = "content/design-thinking";
const syllabusFilePath = "content/syllabuses/data-eng-part-1.md";

const syllabusContent = fs.readFileSync(syllabusFilePath, "utf-8");
const syllabusPaths = extractContentPaths(syllabusContent);

const orphanNodes = findOrphanNodes(contentDirectory, syllabusPaths);

for (const orphanNodeDir of orphanNodes) {
  const indexPath = path.join(orphanNodeDir, "_index.md");
  const indexContent = fs.readFileSync(indexPath, "utf-8");
  
  const db_idMatch = indexContent.match(/_db_id: (\d+)/);
  const titleMatch = indexContent.match(/title: ([^\n]+)/);

  const db_id = db_idMatch ? db_idMatch[1] : "N/A";
  const title = titleMatch ? titleMatch[1] : "N/A";

  console.log(`Orphan node directory: ${orphanNodeDir}`);
  console.log(`Title: ${title}`);
  console.log(`_db_id: ${db_id}`);
  console.log("-----------------------------------");
}

console.log("Script finished.");
