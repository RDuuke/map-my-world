class BaseRepository:
    """
    A base class for repositories providing common functionality.
    """

    @staticmethod
    def rename_id(data):
        """
        Renames the '_id' key to 'uuid' in a dictionary.

        This static method takes a dictionary as input and returns a new dictionary
        where the key '_id' (if present) is renamed to 'uuid'. This is useful when
        dealing with data from MongoDB, where the primary key is typically named '_id',
        but you might want to use a more standard 'id' or 'uuid' field in your application.

        Args:
            data (dict): The dictionary to process.

        Returns:
            A new dictionary with the '_id' key renamed to 'uuid' (if it existed).
        """
        return {('uuid' if key == '_id' else key): value for key, value in data.items()}