# lsp_exercise.py

from dataclasses import dataclass, field
from typing import List


@dataclass
class FinancialDocument: 
    customer: str
    items: List[dict]
    total: float = field(init=False)

    def __post_init__(self):
        """Calcula el total sumando el precio de los items."""
        self.total = sum(item['price'] for item in self.items)
    

# El problema está en esta jerarquía
@dataclass
class Invoice(FinancialDocument):
    """Representa un documento de cobro."""
    def __post_init__(self):
        # Llamamos al __post_init__ del padre para no repetir el cálculo del total.
        super().__post_init__()

@dataclass
class CreditNote(FinancialDocument):
    """Representa una devolución. Viola LSP porque añade una excepción que el padre no tiene."""
    reason: str

    def __post_init__(self):
        # Llamamos al __post_init__ del padre para no repetir el cálculo del total.
        super().__post_init__()
        
        # ¡VIOLACIÓN! El padre nunca lanza este error.
        # Un código que funciona con Invoice se romperá si le pasas esta clase hija.
        if self.total > 0:
            raise ValueError("Una nota de crédito no puede tener un total positivo.")


# --- Script principal que demuestra el problema ---
def main():
    # Una factura normal funciona bien
    invoice = Invoice(customer="Cliente A", items=[{'name': 'Producto 1', 'price': 100}])
    print(f"Factura válida creada: Total {invoice.total}")

    # Una nota de crédito con items negativos funciona bien
    credit_note_valid = CreditNote(
        customer="Cliente B", 
        items=[{'name': 'Devolución Producto 2', 'price': -50}],
        reason="Producto defectuoso"
    )
    print(f"Nota de crédito válida creada: Total {credit_note_valid.total}")

    # Lista de "facturas" a procesar
    documents:List[FinancialDocument] = [invoice, credit_note_valid] 

    print("\nProcesando documentos válidos...")
    for doc in documents:
        # Este código confía en que cualquier "Invoice" es seguro de procesar
        print(f"Procesando documento para {doc.customer} con total {doc.total}")
    
    print("\n--- AHORA EL CASO QUE ROMPE EL PROGRAMA ---")
    try:
        # Creamos una nota de crédito inválida
        credit_note_invalid = CreditNote(
            customer="Cliente C", 
            items=[{'name': 'Item con precio positivo', 'price': 25}], # Esto debería ser -25
            reason="Error de entrada"
        )
        print(f'Nota de credito invalida: {credit_note_invalid}')
    except ValueError as e:
        print(f"Error al crear la nota de crédito inválida: {e}")


if __name__ == "__main__":
    main()