"""
This is the in-memory database.

Because its in-memory, it can be modified, but it will be reset to this
state after the server restarts.

Normally you would use a real database like PostgreSQL, MySQL, SQLite, etc.

But if you are here before level 4, you can just manually add
more users/bricks.


🤯 Level >9000: Super L33t Hacker Code Max Problem:
     If you have got through level 3, you can implement a persistent database.
     You can modify this so instead of having a dictionary, it reads/writes
     to/from a JSON file.
"""

database = {
    "users": {
        "mahum": {"name": "mahum", "role": 5000, "groups": ["mahum"]},
        "isaac": {"name": "isaac", "role": 4000, "groups": ["isaac"]},
        "admin": {"name": "admin", "role": 4000, "groups": ["admins"]},
        "super": {"name": "super", "role": 9001, "groups": []},
        "public": {"name": "public", "role": 1000, "groups": ["public"]},
    },
    "bricks": {
        "red": {"color": "red", "allowed_role": 5000, "allowed_groups": ["mahum", "isaac"]},
        "blue": {"color": "blue", "allowed_role": 3000, "allowed_groups": ["admins"]},
        "green": {"color": "green", "allowed_role": 1000, "allowed_groups": ["public"]},
        "yellow": {"color": "yellow", "allowed_role": 4000, "allowed_groups": ["admins"]},
        "black": {"color": "black", "allowed_role": 2000, "allowed_groups": ["public"]},
    },
}
