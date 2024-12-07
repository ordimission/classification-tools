import os
import xml.etree.ElementTree as ET
import xml.dom.minidom

def create_outline(element, path):
    """
    Ajoute des éléments dans l'arborescence XML en fonction de l'arborescence des fichiers,
    seulement les noms de fichiers en majuscules et continue de descendre dans les sous-répertoires.
    """
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path) and item.isupper():
                outline = ET.SubElement(element, "outline", {"text": item, "type": "folder"})
                create_outline(outline, item_path)  # Descendre dans les sous-répertoires
    except PermissionError:
        print(f"Permission denied: {path}")
        ET.SubElement(element, "outline", {"text": "Permission denied", "type": "error"})

def generate_opml(root_dir, output_file):
    """
    Génère un fichier OPML à partir de l'arborescence du répertoire spécifié.
    """
    opml = ET.Element("opml", {"version": "2.0"})
    head = ET.SubElement(opml, "head")
    ET.SubElement(head, "title").text = "Fichier OPML de l'arborescence des fichiers"
    
    body = ET.SubElement(opml, "body")
    create_outline(body, root_dir)
    
    # Pretty print du fichier OPML
    rough_string = ET.tostring(opml, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(reparsed.toprettyxml(indent="  "))

def main():
    root_dir = "D:/"  # Remplacez par le chemin de votre répertoire
    output_file = "arborescence.opml"  # Nom du fichier de sortie OPML
    
    generate_opml(root_dir, output_file)
    print(f"Fichier OPML généré : {output_file}")

if __name__ == "__main__":
    main()
