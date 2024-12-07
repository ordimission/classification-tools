import os
import xml.etree.ElementTree as ET

def create_directory_structure(element, base_path):
    """
    Recrée l'arborescence des fichiers à partir de l'élément XML OPML.
    """
    for outline in element.findall("outline"):
        text = outline.get("text")
        node_type = outline.get("type")
        if node_type == "folder":
            dir_path = os.path.join(base_path, text)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            create_directory_structure(outline, dir_path)
        elif node_type == "file":
            file_path = os.path.join(base_path, text)
            with open(file_path, 'w') as f:
                f.write("")  # Crée un fichier vide

def parse_opml_and_create_structure(opml_file, root_dir):
    """
    Parse le fichier OPML et recrée l'arborescence des fichiers.
    """
    tree = ET.parse(opml_file)
    root = tree.getroot()
    body = root.find("body")
    create_directory_structure(body, root_dir)

def main():
    opml_file = "arborescence.opml"  # Remplacez par le chemin de votre fichier OPML
    root_dir = "T:/"  # Remplacez par le chemin du répertoire de destination
    
    parse_opml_and_create_structure(opml_file, root_dir)
    print(f"Arborescence recréée dans le répertoire : {root_dir}")

if __name__ == "__main__":
    main()
