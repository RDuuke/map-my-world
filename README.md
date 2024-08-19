# Map My World - Backend API

Este proyecto implementa el backend de la aplicación "Map My World", que permite a los usuarios explorar y revisar diferentes ubicaciones y categorías en todo el mundo. La API proporciona endpoints para gestionar ubicaciones, categorías y reseñas, así como para obtener recomendaciones de exploración basadas en la actividad de revisión.
Características principales

- Gestión de ubicaciones: Permite crear nuevas ubicaciones especificando sus coordenadas de latitud y longitud.
- Gestión de categorías: Permite crear nuevas categorías para clasificar las ubicaciones.
- Gestión de reseñas: Permite crear y actualizar reseñas que asocian ubicaciones con categorías, registrando la fecha de la última revisión.
- Recomendaciones de exploración: Sugiere combinaciones de ubicación-categoría que no han sido revisadas recientemente o que nunca han sido revisadas, priorizando estas últimas.

## Tecnologías utilizadas

- FastAPI: Framework web moderno y rápido para construir APIs REST en Python.
- MongoDB: Base de datos NoSQL orientada a documentos para almacenar los datos de la aplicación.
- Motor: Driver asíncrono para Python que permite interactuar con MongoDB de manera eficiente.
- Pydantic: Biblioteca para definir modelos de datos y realizar validación de entrada/salida.
- Dependency Injector: Biblioteca para implementar inyección de dependencias y mejorar la organización y mantenibilidad del código.

## Estructura del proyecto

- src/api/: Contiene los endpoints de la API y la lógica de enrutamiento.
- internal/: Contiene los módulos internos de la aplicación, como los modelos de datos, los casos de uso, los handlers y los repositorios.
- requirements.txt: Lista las dependencias del proyecto.
- docker-compose.yml: Define los servicios de Docker (aplicación FastAPI y MongoDB) y su configuración.
- Dockerfile: Describe cómo construir la imagen de Docker para la aplicación FastAPI.
- Dockerfile.mongodb: Describe cómo construir la imagen de Docker para MongoDB con mongosh.

### Patrones de diseño

- Inyección de dependencias: El uso de un contenedor de dependencias y la función Depends de FastAPI para inyectar las dependencias necesarias en los handlers y casos de uso es un claro ejemplo de este patrón. Esto promueve el desacoplamiento entre los componentes y facilita las pruebas unitarias.

- Repositorio: La clase abstracta BaseRepository y sus implementaciones concretas (como LocationMongoRepository) siguen el patrón de repositorio. Esto separa la lógica de acceso a datos del resto de la aplicación, lo que facilita el cambio de la fuente de datos en el futuro si es necesario.

- Caso de uso: Las clases como LocationCreateUseCase representan casos de uso específicos de la aplicación. Encapsulan la lógica de negocio relacionada con una acción particular, lo que hace que el código sea más organizado y reutilizable.

- Handler (manejador): Las clases como LocationCreateHandler actúan como intermediarios entre los endpoints de la API y los casos de uso. Reciben las solicitudes, realizan validaciones adicionales si es necesario y luego llaman al caso de uso correspondiente.

- Data Transfer Object (DTO): Las clases LocationCreateCommand, ReviewCreateCommand, etc., pueden considerarse DTOs, ya que se utilizan para transferir datos entre diferentes capas de la aplicación.

### Arquitectura

- Arquitectura limpia (Clean Architecture): Aunque no se implementa de forma estricta, la estructura del código se asemeja a algunos principios de la arquitectura limpia, como la separación de responsabilidades en capas (API, handlers, casos de uso, repositorios) y la dependencia de las capas internas hacia las capas externas.
- Modelo-Vista-Controlador (MVC): De manera similar, la estructura también tiene similitudes con el patrón MVC, donde los modelos representan los datos (Location, Category, etc.), las vistas son los endpoints de FastAPI, y los controladores son los handlers que manejan las solicitudes y llaman a los casos de uso.

### Otras consideraciones

- Patrón de fábrica: El uso de providers.Factory en el contenedor de dependencias puede considerarse una implementación del patrón de fábrica, ya que se encarga de crear nuevas instancias de los objetos (repositorios, casos de uso, handlers) cuando son solicitados.
- SOLID: La estructura del código promueve algunos de los principios SOLID, como la responsabilidad única (cada componente tiene una función clara y bien definida) y la inversión de dependencias (los componentes dependen de abstracciones en lugar de implementaciones concretas).

## Cómo ejecutar la aplicación

### Clonar el repositorio:
    
``` bash
git clone https://github.com/RDuuke/map-my-world
```

### Levantar los servicios con Docker Compose:
``` bash
docker-compose up -d
```