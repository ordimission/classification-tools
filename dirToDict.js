const fs = require('fs');
const path = require('path');

function dirToDict(currentPath) {
    let tree = {};

    function helper(currentPath, currentDict) {
        try {
            const entries = fs.readdirSync(currentPath, { withFileTypes: true });
            for (const entry of entries) {
                if (entry.isDirectory() && entry.name === entry.name.toUpperCase()) {
                    currentDict[entry.name] = {};
                    helper(path.join(currentPath, entry.name), currentDict[entry.name]);
                }
            }
        } catch (err) {
            if (err.code === 'EACCES') {
                console.error(`Permission denied: ${currentPath}`);
                currentDict["error"] = "Permission denied";
            } else {
                console.error(`An error occurred: ${err.message}`);
                currentDict["error"] = err.message;
            }
        }
    }

    helper(currentPath, tree);
    return tree;
}

function main() {
    const dirPath = "E:/";  // Remplacer par le chemin du répertoire que vous souhaitez parcourir
    const tree = dirToDict(dirPath);
    fs.writeFileSync("filesystem.json", JSON.stringify(tree, null, 4), 'utf8');
}

main();
