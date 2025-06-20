"""

El Escenario
Imagina que trabajas para una empresa de e-commerce. El equipo de marketing necesita un sistema para enviar notificaciones a los usuarios sobre nuevas promociones.

Requisitos Iniciales (Versión 1):

- El sistema debe obtener la lista de usuarios de una base de datos.
- Debe formatear un mensaje de promoción para ser enviado por Email.
- Debe enviar el email a cada usuario.
- Debe registrar (log) cada envío exitoso en un archivo de texto local (log.txt).
- Requisitos Futuros (Pistas para tu Diseño):

El jefe de producto ya te ha adelantado que en los próximos meses querrán:

Añadir notificaciones por SMS.
A veces, obtener la lista de usuarios de un archivo CSV que el equipo de marketing subirá.
Posiblemente, añadir notificaciones Push a la aplicación móvil.
Cambiar el logging para que en lugar de un archivo, se envíe a un servicio externo como Sentry o se guarde en otra tabla de la base de datos.
Tu tarea es diseñar la Versión 1 de tal manera que añadir estas futuras funcionalidades sea trivial y no requiera modificar las clases existentes.

"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

 
@dataclass
class User: 
   username: str
   email: str

class IUserRepository(ABC): 
    @abstractmethod
    def get_users(self) -> list[User]:   ...

class INotifierSenderRepository(ABC):
    @abstractmethod
    def send_notification(self, user_data: User, message: str):
        ...

class IFormatterRepository(ABC):
    @abstractmethod
    def format(self, user: User, message:str) -> str: ...
   
class IRegisterLoggerRepository(ABC):
    @abstractmethod
    def log(self, user:User, filename: str = 'Registro.txt') -> str: ...

class UserRepository(IUserRepository):

    def get_users(self) -> list[User]:
        print("Obteniendo usuarios desde la Base de Datos...")
        return [User('Joel', 'Joel@joe.com '),User('Juan', 'Juan@juan.com')]
        
@dataclass
class EmailNotifier(INotifierSenderRepository):

    promotion_code:str
    def send_notification(self, user_data: User, message: str):
        print(f"-> Enviando Email a: {user_data.email} | Mensaje: '{message}' | Código: {self.promotion_code}")
        ...

class SMSNotifier(INotifierSenderRepository):
    def send_notification(self, user_data: User, message: str):
        print(f"-> Enviando SMS a: {user_data.username} | Mensaje: '{message}'")
         
class MessageFormat(IFormatterRepository):
     def format(self, user: User, message:str) -> str:
        return f"Hola {user.username}, {message}"

class FileLogger(IRegisterLoggerRepository):
    def log(self, user: User, filename: str = "Registro.txt")-> str:
        with open(filename, 'a') as f:
           f.write(f"Notificación enviada a {user.username} ({user.email})\n")
        return f'{filename} de {user.username}'
    
@dataclass
class NotificationServices:

    users: IUserRepository
    sender: INotifierSenderRepository
    message_formatter: IFormatterRepository
    logs: IRegisterLoggerRepository

    def send_promotional_notificacion(self, message: str): 
        for user in self.users.get_users():
            format_message = self.message_formatter.format(user, message) 
            self.sender.send_notification(user, format_message)
            self.logs.log(user, filename='Promotion.txt')

if __name__ == '__main__': 

    user = UserRepository()
    email_notifier = EmailNotifier(promotion_code='08G0142')
    formatter = MessageFormat()
    file_logger = FileLogger()
    notification = NotificationServices(user,email_notifier,formatter,file_logger)
    notification.send_promotional_notificacion('Hola tienes un nueva notificacion😇')
    

    