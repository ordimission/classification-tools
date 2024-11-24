import os
import json

def dir_to_dict(path):
    tree = {}
    def helper(current_path, current_dict):
        try:
            for entry in os.listdir(current_path):
                full_path = os.path.join(current_path, entry)
                if os.path.isdir(full_path) and entry.isupper():
                    current_dict[entry] = {}
                    helper(full_path, current_dict[entry])
        except PermissionError:
            print(f"Permission denied: {current_path}")
            current_dict["error"] = "Permission denied"
        except Exception as e:
            print(f"An error occurred: {e}")
            current_dict["error"] = str(e)
    helper(path, tree)
    return tree

def main():
    path = "D:/"  # Remplacer par le chemin du répertoire que vous souhaitez parcourir
    tree = dir_to_dict(path)
    with open("filesystem.json", "w", encoding='utf-8') as f:
        json.dump(tree, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
