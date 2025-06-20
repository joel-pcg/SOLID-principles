# ocp_exercise.py

import json
from dataclasses import dataclass, field
from typing import List
from abc import abstractmethod, ABC

@dataclass
class Invoice:
    """Contenedor de datos para una factura."""
    customer: str
    items: List[dict]
    total: float = field(init=False)

    def __post_init__(self):
        self.total = sum(item['price'] for item in self.items)


class InvoiceFormatterStrategy(ABC):
    @abstractmethod
    def format(self, invoice: Invoice) -> str:...

class JsonFormatter(InvoiceFormatterStrategy):
    """Esto es lo que vamos a refactorizar para que cumpla OCP."""
    def format(self, invoice: Invoice) -> str:
        return json.dumps({
            'customer': invoice.customer,
            'items': invoice.items,
            'total': invoice.total
        }, indent=4)

class PlainFormatter(InvoiceFormatterStrategy):

    def format(self, invoice:Invoice) -> str :

        plain_text = f"""
        Factura para: {invoice.customer}
        Total: ${invoice.total}
        Items:
        """

        for item in invoice.items: 
            plain_text += f' -{item['name']}: ${item['price']}\n'
        return plain_text

    

# (La clase InvoiceRepository puede quedar como está, no nos afecta ahora)
class InvoiceRepository:
    def save_to_file(self, invoice_data: str, filename: str):
        with open(filename, 'w') as f:
            f.write(invoice_data)
        print(f"Factura guardada en {filename}")


# --- Script principal ---
def main():
    invoice_items = [
        {'name': 'SSD 1TB', 'price': 95.00}, 
        {'name': 'RAM 16GB', 'price': 80.00}
    ]
    my_invoice = Invoice(customer="Ana Torres", items=invoice_items)
    
    json_format = JsonFormatter()
    plain_format = PlainFormatter()

    repository = InvoiceRepository()
    
    # Aquí solo podemos formatear a JSON
    invoice_as_json = json_format.format(my_invoice)
    invoice_as_plain_text = plain_format.format(my_invoice)

    repository.save_to_file(invoice_as_json, "invoice.json")
    repository.save_to_file(invoice_as_plain_text, "invoice.txt")
    
    # ¿Cómo podríamos añadir un formato de texto plano aquí de forma elegante?

if __name__ == "__main__":
    main()