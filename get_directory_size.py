import os
import json

def get_directory_size_and_file_count(path):
    total_size = 0
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp) and os.path.isfile(fp):
                total_size += os.path.getsize(fp)
                file_count += 1
    return total_size, file_count

def dir_to_dict(path, level):
    def helper(current_path, current_level):
        if current_level > level:
            return None, 0, 0
        tree = {}
        total_size = 0
        total_files = 0
        try:
            for entry in os.listdir(current_path):
                full_path = os.path.join(current_path, entry)
                if os.path.isdir(full_path):
                    if current_level < level:
                        subtree, sub_size, sub_files = helper(full_path, current_level + 1)
                        if subtree is not None:
                            tree[entry] = subtree
                            total_size += sub_size
                            total_files += sub_files
                    else:
                        dir_size, file_count = get_directory_size_and_file_count(full_path)
                        tree[entry] = {"size": dir_size, "file_count": file_count}
                        total_size += dir_size
                        total_files += file_count
            return tree, total_size, total_files
        except PermissionError:
            print(f"Permission denied: {current_path}")
            return None, 0, 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, 0, 0

    tree, _, _ = helper(path, 0)
    return tree

def main():
    path = "D:\\MASTERS\\CODE\\ASSOCIATIONS\\AVF\\audiovie"  # Remplacer par le chemin du répertoire que vous souhaitez parcourir
    level = 2  # Remplacer par le niveau d'arborescence que vous souhaitez
    tree = dir_to_dict(path, level)
    with open("filesystemsize.json", "w", encoding='utf-8') as f:
        json.dump(tree, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()

