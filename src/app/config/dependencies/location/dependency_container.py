import os

from dependency_injector import containers, providers

from internal.location.repository import LocationMongoRepository
from internal.location.use_case import LocationCreateUseCase, LocationGetAllUseCase
from src.api.handler.location import LocationCreateHandler, LocationGetAllHandler


class LocationDependencyContainer(containers.DeclarativeContainer):
    """
    Dependency container for managing locations.

    This container defines providers for the location repository, the location creation use case,
    and the corresponding handler. The choice of repository is based on the 'ENV' environment variable.
    """

    environment = os.environ.get('ENV', 'mongo_dev')
    """
    Gets the value of the 'ENV' environment variable, defaults to 'mongo_dev'
    """

    location_repository = providers.Factory(
        lambda: LocationMongoRepository()
        if LocationDependencyContainer.environment == 'mongo_dev' else None
    )
    """
    Provides an instance of the location repository.

    If the 'ENV' environment variable is equal to 'mongo_dev', it uses the `LocationMongoRepository`.
    Otherwise, it returns None (which could cause an error if the repository is attempted to be used).
    """

    location_create_use_case = providers.Factory(
        LocationCreateUseCase,
        repository=location_repository,
    )
    """
    Provides an instance of the `LocationCreateUseCase`.

    Injects the location repository (`location_repository`) as a dependency into the use case.
    """

    location_geT_all_use_case = providers.Factory(
        LocationGetAllUseCase,
        repository=location_repository
    )

    location_create_handler = providers.Factory(
        LocationCreateHandler,
        use_case=location_create_use_case,
    )
    """
    Provides an instance of the `LocationCreateHandler`.

    Injects the location creation use case (`location_create_use_case`) as a dependency into the handler.
    """

    location_get_all_handler = providers.Factory(
        LocationGetAllHandler,
        use_case=location_geT_all_use_case
    )
