# isp_final.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class Document:
    doc_id: int
    content: str

# --- Interfaces Segregadas y con un propósito único ---

class IWritableRepository(ABC):
    @abstractmethod
    def save(self, document: Document):
        """Guarda un documento."""
        ...

class IReadableRepository(ABC): 
    @abstractmethod
    def find_by_id(self, doc_id: int) -> Document:
        """Busca un documento por su ID."""
        ...
    @abstractmethod
    def get_all_by_content(self, query: str) -> List[Document]:
        """Busca todos los documentos que contengan un texto."""
        ...

# --- Implementaciones que heredan solo los contratos que necesitan ---

class DatabaseRepository(IWritableRepository, IReadableRepository):
    """Implementa AMBOS roles de escritura y lectura."""
    def save(self, document: Document):
        print(f"  -> Guardando doc {document.doc_id} en la base de datos.")
    
    def find_by_id(self, doc_id: int) -> Document:
        print(f"  -> Buscando doc {doc_id} en la base de datos.")
        return Document(doc_id, "Contenido desde la BD")

    def get_all_by_content(self, query: str) -> List[Document]:
        print(f"  -> Buscando documentos con '{query}' en la base de datos.")
        return [Document(1, "Contenido"), Document(2, "Otro contenido")]

class FileRepository(IWritableRepository):
    """Implementa SOLAMENTE el rol de escritura."""
    def save(self, document: Document):
        print(f"  -> Guardando doc {document.doc_id} en un archivo de texto.")

# --- Funciones cliente que dependen de las interfaces pequeñas ---

def save_documents(repo: IWritableRepository, docs: List[Document]): 
    # REFINAMIENTO 1: Procesar todos los documentos.
    print(f"Usando {repo.__class__.__name__} para guardar {len(docs)} documento(s)...")
    for doc in docs:
        repo.save(doc)

def search_documents(repo: IReadableRepository, query: str) -> List[Document]: 
    print(f"Usando {repo.__class__.__name__} para buscar documentos...")
    return repo.get_all_by_content(query)
    
# --- Código Cliente ---
def main():
    db_repo = DatabaseRepository()
    file_repo = FileRepository()
    docs_to_save = [Document(101, "SOLID"), Document(102, "ISP")]

    # La función save_documents funciona con CUALQUIER repositorio que sea "escribible".
    save_documents(db_repo, docs_to_save)
    print("-" * 20)
    save_documents(file_repo, docs_to_save)
    print("-" * 20)

    # La función search_documents solo funciona con repositorios "leíbles".
    # REFINAMIENTO 2: Capturar y mostrar el resultado.
    found_docs = search_documents(db_repo, query='SOLID')
    print(f"Resultado de la búsqueda: {found_docs}")

    # ¡Esto daría un error con un analizador de tipos como MyPy, lo cual es genial!
    # search_documents(file_repo, query='test') # -> Error: Expected IReadableRepository, got FileRepository

if __name__ == "__main__":
    main()