from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from .schemas import AppointmentCreate, AppointmentRead



class IAppointmentRepository(ABC):

    """
    Define el contrato para las operaciones de persistencia de citas.
    Cualquier clase de repositorio de citas deberá implementar estos métodos.
    de esta forma respeta el OCP 
    """

    @abstractmethod
    def get_by_date(self, appointment_date: datetime) -> Optional[AppointmentRead]: 
        """
        Busca una cita por su fecha y hora exactas.
        Devuelve la cita si la encuentra, o None si el horario está libre.
        """
        ...
    @abstractmethod
    def create(self, appointment: AppointmentCreate) -> AppointmentRead:
        """
        Guarda una nueva cita en el sistema de persistencia.
        Devuelve la cita creada, incluyendo su nuevo ID.
        """
        ...

    @abstractmethod
    def get_all(self) ->list[AppointmentRead]: 
        """
        Devuelve todas las citas almacenadas.
        Útil para listar todas las citas en el sistema.
        """
        ...
    @abstractmethod
    def get_by_id(self, id: int) -> AppointmentRead | None:
        """
        Devuelve  las citas almacenadas con el ID seleccionado.
        Útil para listar  citas especificas en el sistema.
        """
        ...



class InMemoryAppointmentRepository(IAppointmentRepository):

    def __init__(self): 
        self._appointments: dict[int, AppointmentRead] = {}
        self._next_id: int = 1
        print("Repositorio inicializado")

    def get_by_date(self, appointment_date: datetime) -> AppointmentRead | None:
        print(f"Buscando cita para la fecha: {appointment_date}")
        for appointment in self._appointments.values():
            print(f"Comparando con cita existente: {appointment.appointment_date}")
            # Convertir ambas fechas a UTC y remover tzinfo para comparación
            date1 = appointment.appointment_date.replace(microsecond=0, tzinfo=None)
            date2 = appointment_date.replace(microsecond=0, tzinfo=None)
            if date1 == date2:
                print(f"¡Cita encontrada! ID: {appointment.id}")
                return appointment
        print("No se encontró cita para esta fecha")
        return None

    def create(self, appointment: AppointmentCreate) -> AppointmentRead:
        print(f"Creando nueva cita con ID: {self._next_id}")
        new_id = self._next_id
        self._next_id += 1

        appointment_data = appointment.model_dump()
        new_appointment = AppointmentRead(id=new_id, **appointment_data)
        self._appointments[new_id] = new_appointment
        print(f"Cita creada. Total de citas: {len(self._appointments)}")
        return new_appointment

    def get_all(self) -> list[AppointmentRead]:
        return list(self._appointments.values())


    def get_by_id(self, id: int) -> AppointmentRead | None:
        """
        Devuelve  las citas almacenadas con el ID seleccionado.
        Útil para listar  citas especificas en el sistema.
        """
        ...
        return self._appointments.get(id, None)