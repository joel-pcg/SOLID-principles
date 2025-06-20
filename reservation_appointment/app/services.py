# Importamos las abstracciones y schemas que el servicio necesita conocer
from .repositories import IAppointmentRepository
from .schemas import AppointmentCreate, AppointmentRead


class AppointmentService:
    """
    Contiene la lógica de negocio para manejar las citas.
    Depende de la abstracción del repositorio, no de una implementación concreta.
    """
    def __init__(self, repo: IAppointmentRepository):
        # Inyección de Dependencias: El servicio recibe la "herramienta" que necesita
        self.repo = repo

    def create_appointment(self, appointment_data: AppointmentCreate) -> AppointmentRead:
        """
        Lógica para crear una nueva cita, aplicando las reglas de negocio.
        """
        
        # 1. Verificar si existe una cita en esta fecha/hora
        existing_appointment = self.repo.get_by_date(appointment_data.appointment_date)
        
        # 2. Si existe, lanzar error
        if existing_appointment:  # Cambio importante aquí
            print("Service: ¡Conflicto! Ya existe una cita para esta fecha")
            raise ValueError('El horario seleccionado ya está ocupado.')
        
        print("Service: Horario libre, procediendo a crear la cita")
        # 3. Si el horario está libre, crear la nueva cita
        new_appointment = self.repo.create(appointment_data)
        print(f"Service: Cita creada exitosamente con ID: {new_appointment.id}")
        
        return new_appointment

    def get_all_appointments(self) -> list[AppointmentRead]:
        """
        Devuelve todas las citas almacenadas.
        """
        print("Service: Obteniendo todas las citas")
        return self.repo.get_all()
    
    def get_appointment_by_id(self, id: int) -> AppointmentRead :
        """
        Devuelve una cita específica por su ID.
        """
        print(f"Service: Buscando cita con ID: {id}")
        appointment = self.repo.get_by_id(id)
        if not appointment:
            print(f"Service: No se encontró cita con ID: {id}")
            raise ValueError('No appointment found with this ID')
        return appointment