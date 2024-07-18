from fastapi import APIRouter, HTTPException
from typing import List, Optional
from .database import database

router = APIRouter()


@router.get("/bricks", response_model=List[dict])
def get_bricks() -> List[dict]:
    """
    🌟 Level 1: Retrieve all bricks from the database and return them to the client
    """
    return list(database["bricks"].values())


@router.get("/users", response_model=List[dict])
def get_users() -> List[dict]:
    """
    🌟 Level 1:  Retrieve all users from the database and return them to the client
    """
    raise HTTPException(status_code=501, detail="users")


@router.get("/users/{name}")
def get_user(name: str) -> dict:
    """
    🌟 Level 1:
             Find the user with the given name and return it to the client
             If the user does not exist, return a 404 error (raise HTTPException(status_code=404))
    """
    #raise HTTPException(status_code=501, detail="Not implemented....... yet!")

    user = database["users"].get(name)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.get("/bricks/{color}")
def get_brick(color: str, user: Optional[str] = None) -> dict:
    """
    🌟 Level 1:
             Find the brick with the given color and return it to the client
             If the brick does not exist, return "404 Not Found"
                 (raise HTTPException(status_code=404))

    💥 Level 3:
             For level 3, get the user with the given name and check if they can
             access the brick. You will have to implement the can_access function
             according to the "Permission System" in the readme.

             If the user does not exist, return "404 Not Found"  (raise HTTPException(status_code=404))
             If the user does not have access to the brick, return a "401 Not Authorized"
             (raise HTTPException(status_code=401))
             If the user does have access to the brick, return the brick!
    """
    #raise HTTPException(status_code=501, detail="Not implemented....... yet!")

    brick = database["bricks"].get(color)
    if not brick:
        raise HTTPException(status_code=404, detail="Brick not found")

    if user:
        user_data = database["users"].get(user)
        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")
        if not can_access(user_data, brick):
            raise HTTPException(status_code=401, detail="Not Authorized")
    
    return brick


@router.post("/bricks")
def create_brick(brick: dict) -> dict:
    """
    🚀 Level 2:
            Create a new brick with the given data and add it to the database
            If a brick with the same color already exists, return a "400 Bad Request"
            (raise HTTPException(status_code=400))
            If the brick is successfully created, return the brick!
    """
    #raise HTTPException(status_code=501, detail="Not implemented....... yet!")
    if brick["color"] in database["bricks"]:
        raise HTTPException(status_code=400, detail="Brick already exists")
    
    database["bricks"][brick["color"]] = brick
    return brick


@router.post("/users")
def create_user(user: dict) -> dict:
    """
    🚀 Level 2:
            Create a new user with the given data and add it to the database
            If a user with the same name already exists, return a "400 Bad Request"
            (raise HTTPException(status_code=400))
            If the user is successfully created, return the user!
    """
    raise HTTPException(status_code=501, detail="Not implemented....... yet!")


def can_access(user: dict, brick: dict) -> bool:
    """
    💥 Level 3:
            This function should return True if the user has access to the brick, and False otherwise.
            The user has access to the brick if:
                - The user's role is greater than or equal to the brick's allowed role and
                - The user is in one of the groups allowed to access the brick

            All super users (ones with a role of 9001) have access to all bricks,
            regardless of their groups.

            Return True if the user has access to the brick, and False otherwise.
    """
    return False
