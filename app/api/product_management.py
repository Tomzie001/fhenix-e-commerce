from fastapi import APIRouter

router = APIRouter()


# registration
router.post("/sign-up")
def registration():

    return{"status": "success"}