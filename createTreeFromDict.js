const fs = require('fs');
const path = require('path');

function createTreeFromDict(tree, rootPath) {
    for (const key in tree) {
        if (tree[key] !== null && typeof tree[key] === 'object') {
            const newDirPath = path.join(rootPath, key);
            if (!fs.existsSync(newDirPath)) {
                fs.mkdirSync(newDirPath, { recursive: true });
            }
            createTreeFromDict(tree[key], newDirPath);
        }
    }
}

function main() {
    const jsonPath = "./filesystem.json";  // Le fichier JSON généré
    const outputPath = "./output_directory";  // Le répertoire où recréer l'arborescence

    const tree = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

    if (!fs.existsSync(outputPath)) {
        fs.mkdirSync(outputPath, { recursive: true });
    }

    createTreeFromDict(tree, outputPath);
}

main();
