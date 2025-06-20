# dip_exercise.py
# (Copia aquí las interfaces IWritableRepository, IReadableRepository y las clases
# DatabaseRepository, FileRepository, y Document del ejercicio anterior de ISP)

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

# --- Abstracciones (Interfaces de la lección anterior) ---
@dataclass
class Document:
    doc_id: int
    content: str

class IWritableRepository(ABC):
    @abstractmethod
    def save(self, document: Document): ...

class IReadableRepository(ABC):
    @abstractmethod
    def find_by_id(self, doc_id: int) -> Document: ...
    @abstractmethod
    def get_all_by_content(self, query: str) -> List[Document]: ...

# --- Detalles (Clases concretas de la lección anterior) ---
class DatabaseRepository(IWritableRepository, IReadableRepository):
    def save(self, document: Document): print(f"DB: Guardando doc {document.doc_id}")
    def find_by_id(self, doc_id: int) -> Document: 
        print(f"DB: Buscando doc {doc_id}")
        return Document(doc_id, "")
    def get_all_by_content(self, query: str) -> List[Document]: 
        print(f"DB: Buscando '{query}'") 
        return [Document(1, "")]

class FileRepository(IWritableRepository):
    def save(self, document: Document): print(f"File: Guardando doc {document.doc_id}")

# --- Módulo de Alto Nivel (El que vamos a refactorizar) ---

class ReportingService:
    """
    Este es nuestro módulo de alto nivel. Actualmente viola DIP
    porque crea sus propias dependencias de bajo nivel.
    """
    def __init__(self, reader: IReadableRepository, writer: IWritableRepository):
        # ¡ACOPLAMIENTO FUERTE! El módulo de alto nivel depende directamente de los detalles.
        self.reader = reader
        self.writer = writer

    def generate_report(self):
        print("--- Iniciando generación de reporte ---")
        docs = self.reader.get_all_by_content("report data")
        report_doc = Document(999, f"Reporte basado en {len(docs)} documento(s).")
        self.writer.save(report_doc)
        print("--- Reporte generado exitosamente ---")

# --- Código Cliente ---
def main():
    # El código cliente es simple, pero el servicio es rígido y difícil de probar.
    db_repo = DatabaseRepository()
    file_repo = FileRepository()
    service = ReportingService(db_repo, file_repo)
    service.generate_report()

if __name__ == "__main__":
    main()