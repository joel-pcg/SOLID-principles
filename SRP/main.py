# invoice_refactor_exercise.py

import json
from dataclasses import dataclass, field
from typing import List

# Puedes usar dataclasses para tener un contenedor de datos más limpio
@dataclass
class Invoice:
    customer: str
    items: List[dict]
    total: float = field(init=False) # El total no se pasará al crear, se calculará

    def __post_init__(self):
        self.total = sum(item['price'] for item in self.items)
        
    # ¿Deberían estar estos métodos aquí?
    def calculate_total(self):
        """Calcula el total sumando el precio de los items."""
        self.total = sum(item['price'] for item in self.items)



class InvoiceRepository:     
    def save_to_file(self, invoice_data: str ,filename: str = "invoice.txt"):
        """Guarda la factura en un archivo."""
        with open(filename, 'w') as f:
            f.write(invoice_data)
        print(f"Factura guardada en {filename}")



class InvoiceFormatter:
    def to_json(self, invoice: Invoice) -> str:
        """Genera una representación JSON de la factura."""
        return json.dumps({
            'customer': invoice.customer,
            'items': invoice.items,
            'total': invoice.total
        }, indent=4)


# --- Script principal ---
def main():
    invoice_items = [
        {'name': 'Teclado Mecánico', 'price': 150.00},
        {'name': 'Mouse RGB', 'price': 75.50},
        {'name': 'Monitor 27"', 'price': 320.00}
    ]
    
    # ¿Cómo debería cambiar el uso de la clase aquí?
    my_invoice = Invoice(customer="Maria Lopez", items=invoice_items)
    # my_invoice.calculate_total()

    format_invoice  = InvoiceFormatter().to_json(my_invoice)
    print("--- Representación JSON de la Factura ---")
    print(format_invoice)
    
    print("\n--- Guardando la Factura ---")
    InvoiceRepository().save_to_file(format_invoice)



if __name__ == "__main__":
    main()