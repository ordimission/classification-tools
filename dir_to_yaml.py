import os
import yaml

def get_directory_structure(root_dir):
    """
    Crée une représentation de l'arborescence des répertoires avec uniquement les fichiers en majuscules.
    """
    dir_structure = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Sépare le chemin racine du chemin relatif
        relative_path = os.path.relpath(dirpath, root_dir)
        # Filtre les fichiers pour ne garder que ceux en majuscules
        files = {file: None for file in filenames if file.isupper()}
        # Crée une liste des sous-répertoires
        subdirs = {dirname: {} for dirname in dirnames}
        # Associe les fichiers et sous-répertoires au chemin relatif
        if relative_path == ".":
            dir_structure.update(files)
            dir_structure.update(subdirs)
        else:
            d = dir_structure
            for part in relative_path.split(os.sep):
                d = d.setdefault(part, {})
            d.update(files)
            d.update(subdirs)
    return dir_structure

def save_to_yaml(data, yaml_file):
    """
    Sauvegarde les données dans un fichier YAML.
    """
    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

def main():
    root_dir = "D:/"  # Remplacez par le chemin de votre répertoire
    yaml_file = "arborescence.yaml"  # Nom du fichier de sortie YAML

    dir_structure = get_directory_structure(root_dir)
    save_to_yaml(dir_structure, yaml_file)

if __name__ == "__main__":
    main()
