from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/users")
def users(request):
    return {"users": []}