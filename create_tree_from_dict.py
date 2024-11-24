import os
import json

def create_tree_from_dict(tree, root):
    for key, value in tree.items():
        if key == "_files":
            for file in value:
                open(os.path.join(root, file), 'w').close()
        else:
            dir_path = os.path.join(root, key)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            create_tree_from_dict(value, dir_path)

def main():
    with open("filesystem.json", "r") as f:
        tree = json.load(f)
    root_path = "."  # Remplacer par le chemin du répertoire racine où recréer l'arborescence
    create_tree_from_dict(tree, root_path)

if __name__ == "__main__":
    main()
