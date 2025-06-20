# app/main.py

from fastapi import FastAPI, Depends, HTTPException, status

# Importamos todas las piezas de nuestra arquitectura
from .schemas import AppointmentCreate, AppointmentRead
from .services import AppointmentService
from .repositories import IAppointmentRepository, InMemoryAppointmentRepository

# 1. Creamos la instancia de la aplicación FastAPI
app = FastAPI(
    title="API de Reservas de Citas",
    description="Una API para gestionar citas aplicando los principios SOLID.",
    version="1.0.0"
)

# 2. Creamos los "Proveedores" para la Inyección de Dependencias
#    Este es nuestro "Composition Root"
singleton_repo = InMemoryAppointmentRepository()
def get_appointment_repository() -> IAppointmentRepository:
    """
    Proveedor para el repositorio de citas.
    Este es el ÚNICO lugar donde instanciamos una clase concreta.
    Si mañana queremos usar una base de datos real, solo cambiamos esta función.
    """
    return singleton_repo

def get_appointment_service(
    repo: IAppointmentRepository = Depends(get_appointment_repository)
) -> AppointmentService:
    """
    Proveedor para el servicio de citas.
    FastAPI se encarga de resolver la dependencia `get_appointment_repository`
    y nos la pasa automáticamente en el parámetro `repo`.
    """
    return AppointmentService(repo=repo)


# 3. Creamos el Endpoint de la API


@app.get(
    "/appointments",
    response_model=list[AppointmentRead],
    status_code=status.HTTP_200_OK,
    summary="Ver citas"
)
def get_appointment(
    service: AppointmentService = Depends(get_appointment_service)
):
    return service.get_all_appointments()
    ...
@app.get(
    "/appointments/{id}",
    status_code=status.HTTP_200_OK,
    summary="Ver citas por ID"
)
def get_appointment_by_id(
    service: AppointmentService = Depends(get_appointment_service),
    id: int = 1
):
    try:
        return service.get_appointment_by_id(id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@app.post(
    "/appointments",
    response_model=AppointmentRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva cita"
)
def create_new_appointment(
    appointment: AppointmentCreate,
    service: AppointmentService = Depends(get_appointment_service)
):
    """
    Endpoint para crear una nueva cita.
    
    - Recibe los datos de la cita en el cuerpo de la petición.
    - Usa el sistema de dependencias de FastAPI para obtener una instancia del servicio.
    - Maneja los errores de negocio (como citas duplicadas) y los convierte
      en errores HTTP apropiados.
    """
    try:
        # Le pedimos al servicio (lógica de negocio) que cree la cita
        new_appointment = service.create_appointment(appointment)
        return new_appointment
    except ValueError as e:
        # Si el servicio lanza un ValueError (porque la cita está duplicada),
        # lo capturamos y devolvemos un error HTTP 409 Conflict.
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )