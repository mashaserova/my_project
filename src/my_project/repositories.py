from my_project.models import User, Animal


class UserRepository:
    def __init__(self):
        self.__last_id = 0
        self.__table = dict[int, User]()

    async def save(self, user: User) -> None:
        self.__last_id += 1
        user.id = self.__last_id
        self.__table[self.__last_id] = user

    async def get_by_id(self, id: int) -> User | None:
        return self.__table.get(id)

    async def get_by_login(self, login: str) -> User | None:
        for user in self.__table.values():
            if user.login == login:
                return user
        return None

    async def get_by_email(self, email: str) -> User | None:
        for user in self.__table.values():
            if user.email == email:
                return user
        return None

    async def get_all(self) -> list[User]:
        return list(self.__table.values())


class AnimalRepository:
    def __init__(self):
        self.__last_id = 0
        self.__table = dict[int, Animal]()

    async def save(self, animal: Animal) -> None:
        self.__last_id += 1
        animal.id = self.__last_id
        self.__table[self.__last_id] = animal

    async def get_by_id(self, id: int) -> Animal | None:
        return self.__table.get(id)

    async def get_all(self) -> list[Animal]:
        return list(self.__table.values())