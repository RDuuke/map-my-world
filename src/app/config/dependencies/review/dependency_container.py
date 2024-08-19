import os

from dependency_injector import containers, providers

from internal.review.repository import ReviewMongoRepository
from internal.review.use_case import (
    ReviewCreateUseCase,
    ReviewUpdateLastReviewUseCase,
    ReviewRecommendationUseCase,
)
from src.api.handler.review import (
    ReviewRecommendationHandler,
    ReviewCreateHandler,
    ReviewUpdateLastReviewedHandler,
)


class ReviewDependencyContainer(containers.DeclarativeContainer):
    """
    Dependency container for managing reviews.

    This container defines providers for the review repository,
    use cases for creating, updating, and recommending reviews, and
    their corresponding handlers. The choice of repository is based
    on the 'ENV' environment variable.
    """

    environment = os.environ.get('ENV', 'mongo_dev')
    """
    Gets the value of the 'ENV' environment variable, defaults to 'mongo_dev'
    """

    review_repository = providers.Factory(
        lambda: ReviewMongoRepository()
        if ReviewDependencyContainer.environment == 'mongo_dev' else None
    )
    """
    Provides an instance of the review repository. 

    If the 'ENV' environment variable is equal to 'mongo_dev', it uses the `ReviewMongoRepository`.
    Otherwise, it returns None (which could cause an error if the repository is attempted to be used).
    """

    review_create_use_case = providers.Factory(
        ReviewCreateUseCase,
        repository=review_repository,
    )
    """
    Provides an instance of the `ReviewCreateUseCase`.

    Injects the review repository (`review_repository`) as a dependency into the use case.
    """

    review_create_handler = providers.Factory(
        ReviewCreateHandler,
        use_case=review_create_use_case,
    )
    """
    Provides an instance of the `ReviewCreateHandler`.

    Injects the review creation use case (`review_create_use_case`) as a dependency into the handler.
    """

    review_update_last_reviewed_use_case = providers.Factory(
        ReviewUpdateLastReviewUseCase,
        repository=review_repository,
    )
    """
    Provides an instance of the `ReviewUpdateLastReviewUseCase`.

    Injects the review repository (`review_repository`) as a dependency into the use case.
    """

    review_update_last_reviewed_handler = providers.Factory(
        ReviewUpdateLastReviewedHandler,
        use_case=review_update_last_reviewed_use_case,
    )
    """
    Provides an instance of the `ReviewUpdateLastReviewedHandler`.

    Injects the review update last reviewed use case (`review_update_last_reviewed_use_case`) 
    as a dependency into the handler.
    """

    review_recommendation_use_case = providers.Factory(
        ReviewRecommendationUseCase,
        repository=review_repository,
    )
    """
    Provides an instance of the `ReviewRecommendationUseCase`.

    Injects the review repository (`review_repository`) as a dependency into the use case.
    """

    review_recommendation_handler = providers.Factory(
        ReviewRecommendationHandler,
        use_case=review_recommendation_use_case,
    )
    """
    Provides an instance of the `ReviewRecommendationHandler`.

    Injects the review recommendation use case (`review_recommendation_use_case`) 
    as a dependency into the handler.
    """