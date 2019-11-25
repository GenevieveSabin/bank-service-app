class UserSerializer:

    @staticmethod
    def serialize(user):
        return {"name": user.name,
                "pin": user.pin,
                "balance": user.balance}