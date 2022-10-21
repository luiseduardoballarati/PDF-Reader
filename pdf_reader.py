
import fitz 

# Openining the PDF archive
with fitz.open(f"YourArchive.pdf") as pdf:
	texto = ""

	for pagina in pdf:
		texto += f'{pagina.get_text()}\n'

print(texto)