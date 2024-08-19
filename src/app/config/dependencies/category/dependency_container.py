import os
from dependency_injector import providers, containers
from internal.category.repository import CategoryMongoRepository
from internal.category.use_case import CategoryCreateUseCase
from src.api.handler.category import CategoryCreateHandler


class CategoryDependencyContainer(containers.DeclarativeContainer):
    """
    Contenedor de dependencias para la gestión de categorías.

    Este contenedor define los proveedores (providers) para el repositorio de categorías,
    el caso de uso de creación de categorías y el handler correspondiente.
    La elección del repositorio se basa en la variable de entorno 'ENV'.
    """

    environment = os.environ.get('ENV', 'mongo_dev')

    category_repository = providers.Factory(
        lambda: CategoryMongoRepository()
        if CategoryDependencyContainer.environment == 'mongo_dev' else None
    )
    """
    Proporciona una instancia del repositorio de categorías. 

    Si la variable de entorno 'ENV' es igual a 'mongo_dev', se utiliza el `CategoryMongoRepository`.
    De lo contrario, se devuelve None (lo que podría causar un error si se intenta usar el repositorio).
    """

    category_create_use_case = providers.Factory(
        CategoryCreateUseCase,
        repository=category_repository,
    )
    """
    Proporciona una instancia del caso de uso `CategoryCreateUseCase`.

    Inyecta el repositorio de categorías (`category_repository`) como dependencia en el caso de uso.
    """

    category_create_handler = providers.Factory(
        CategoryCreateHandler,
        use_case=category_create_use_case,
    )
    """
    Proporciona una instancia del handler `CategoryCreateHandler`.

    Inyecta el caso de uso de creación de categorías (`category_create_use_case`) como dependencia en el handler.
    """