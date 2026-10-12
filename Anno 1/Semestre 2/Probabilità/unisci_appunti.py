import glob
import re

files = sorted(glob.glob('Appunti_Pro/Pagina_*.md'))
output_path = '9_ValoreAtteso_Completo.md'

with open(output_path, 'w', encoding='utf-8') as outfile:
    outfile.write('# Appunti di Probabilità - 9. Valore Atteso (Completo)\n\n')
    outfile.write(f'> Raccolta unificata: pagine 1 - {len(files)} trascritte e validate.\n\n')
    outfile.write('---\n\n')
    
    for fpath in files:
        match = re.search(r'Pagina_(\d+)\.md', fpath)
        page_num = int(match.group(1)) if match else fpath
        
        with open(fpath, 'r', encoding='utf-8') as infile:
            content = infile.read().strip()
            
        content = re.sub(r'^<!--\s*Pagina\s*\d+\s*-->\s*', '', content, flags=re.IGNORECASE)
        
        outfile.write(f'## Pagina {page_num}\n\n')
        outfile.write(content)
        outfile.write('\n\n---\n\n')

print(f'File unificato creato con successo: {output_path} ({len(files)} pagine)')
