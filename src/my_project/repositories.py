from my_project.models import User


class UserRepository:
    def __init__(self):
        self.__last_id = 0
        self.__table = dict[int, User]()

    async def save(self, user: User):
        self.__last_id += 1
        user.id = self.__last_id
        self.__table[self.__last_id] = user

    async def get_by_id(self, id: int) -> User | None:
        return self.__table.get(id)

    async def get_all(self) -> list[User]:
        return list(self.__table.values())
