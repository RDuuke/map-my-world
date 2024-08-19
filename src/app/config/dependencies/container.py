from src.app.config.dependencies.category.dependency_container import CategoryDependencyContainer
from src.app.config.dependencies.location.dependency_container import LocationDependencyContainer
from src.app.config.dependencies.review.dependency_container import ReviewDependencyContainer


class AppContainer:

    @staticmethod
    def init():
        location_container = LocationDependencyContainer()
        category_container = CategoryDependencyContainer()
        review_container = ReviewDependencyContainer()

        location_container.wire(modules=["src.api.routes.location_route", "src.api.handler.location.create_handler"])
        location_container.wire(modules=["src.api.routes.location_route", "src.api.handler.location.get_all_handler"])
        category_container.wire(modules=["src.api.routes.category_route", "src.api.handler.category.create_handler"])
        category_container.wire(modules=["src.api.routes.category_route", "src.api.handler.category.get_all_handler"])
        review_container.wire(modules=["src.api.routes.review_route", "src.api.handler.review.create_handler"])
        review_container.wire(modules=["src.api.routes.review_route", "src.api.handler.review.add_last_reviewed_handler"])
        review_container.wire(modules=["src.api.routes.review_route", "src.api.handler.review.recommendation_handler"])
