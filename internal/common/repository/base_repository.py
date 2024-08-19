class BaseRepository:

    @staticmethod
    def rename_id(data):
        return {('uuid' if key == '_id' else key): value for key, value in data.items()}
