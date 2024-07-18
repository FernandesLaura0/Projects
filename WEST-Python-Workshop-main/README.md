# WEST Python Workshop

1. [🦅 Overview](#-Overview)
2. [👟 Pre-requisites](#-pre-requisites)
3. [🏗️ Getting Started](#-getting-started)
4. [💪 The Challenge](#-the-challenge)
    - [🌟 Level 1: Basic Endpoints for Getting Data](#-level-1-basic-endpoints-for-getting-data)
    - [🚀 Level 2: Create New Resources In the Database](#-level-2-create-new-resources-in-the-database)
    - [💥 Level 3: Access Control](#-level-3-access-control)
    - [🧠 Level 4: Persist Data](#-level-4-persist-data)
    - [🤯 Level >9000: Super L33t Hacker Code Max Problem](#-level-9000-super-l33t-hacker-code-max-problem)
5. [🔐 The Permission System](#-the-permission-system)
6. [📚 Useful Links and Resources](#-useful-links-and-resources)

## 🦅 Overview

This workshop guides you through setting up a Python-based server using FastAPI, 
managing dependencies, and testing endpoints using Postman. The challenge 
is structured in multiple levels, in level 3 you get to implement a simple 
permissions system..

## 👟 Pre-requisites
- Recent version of Python installed
- Postman ([Postman Installation Guide](https://learning.postman.com/docs/getting-started/installation-and-updates/))

## 🏗️ Getting Started

1.  **Take a look at [the git repository](https://github.com/fargusplumdoodle/WEST-Python-Workshop)**
      - Look through the files and the `README.md`

2. **Download the repository**:
    - Click [here](https://github.com/fargusplumdoodle/WEST-Python-Workshop/archive/refs/heads/main.zip) to download the repo
    - Unzip it to your favourite place 
    - Open a terminal in the workshop directory (`cd ./path/to/the/WEST-Python-Workshop`)

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the server**:
    ```bash
   fastapi run --reload
    ```

5. **Import the Postman collection**:
    - Open Postman
    - Go to `File` -> `Import`
    - Drag and drop the file `./WEST Python Challenge.postman_collection.json`
       into Postman

6. **Use Postman collection to make requests to your server**
    - Initially, all the endpoints will return a `501 Not Implemented` error
    - You should be able to complete this whole challenge without
       making any modifications to the postman collection.

## 💪 The Challenge

There are multiple levels to this challenge

### 🌟 Level 1: Basic Endpoints for Getting Data

The first level is about making sure you can make
`GET` requests to list the resources in our "database".

1. **Implement the endpoints to allow the client to list all users/bricks**:
    - `GET /bricks` Should return every brick in the database (already provided)
    - `GET /users` Should return every user in the database

2. **Get a specific user/brick**:
    - `GET /bricks/{color}` should return a specific brick with the specified color
    - `GET /users/{name}` should return a specific user with the specified name

To test these, use the "GET All Bricks", "GET All Users", "GET Brick by color", 
"GET User by name" requests in Postman.

### 🚀 Level 2: Create New Resources In the Database

This level is all about adding new things to the database. 
You can implement the following endpoints to add new bricks/users
to the database.

This includes:
- `POST /bricks` to add a new brick
- `POST /users` to add a new user

Once you are done, the "POST Add New Brick" and "POST Add new User"
requests should be functional in Postman.

### 💥 Level 3: Access Control

You made it through the basics of REST HTTP servers!

Let's kick it up a notch and make sure that the right users have access
to the right bricks!

Let's modify the `GET /brick/{color}/?user={name}` endpoint so
we fetch the user of the specified name from the database, and check
their `role` and `groups` against the `allowed_role` and `allowed_groups`
of the brick.

If the user doesn't have access to the brick, we should return `401 Not Authorized`.

For more information, read about the permission system below!

### 🤯 Level >9000: Super L33t Hacker Code Max Problem

Access Control? No problem.

But you know what is a problem? Our database gets wiped everytime 
the server restarts. This would likely get us fired.

Here lets ditch the in-memory database, and instead modify our
application to store the database in a JSON file. 

This means, everytime you make a new brick/user, it gets written
inside a JSON file. Everytime you read bricks/users, 
they should come from that same file.

This will allow the server to restart without us losing our data!

Good luck, and happy coding!

## 🔐 The Permission System

This is relevant for Level 3.

Each user has a role and a groups list. Each brick has an `allowed_role` and an `allowed_groups` list.

Roles are defined as integers between 0 and 9001:

```python
NOBODY = 0
PUBLIC = 1000
AUTHOR = 2000
EDITOR = 3000
ADMIN = 4000
OWNER = 5000
SUPER = 9001
```

A user's access to a brick is determined by the following rules:

- Super users (`role == 9001`) can access any brick.
- The user must have at least one group in common with the brick.
- The user's role must be equal to or greater than the allowed_role of the brick.


So for example, in this scenario we have a brick and 2 users.

```json
// Brick: Red
{
   "color": "red",
   "allowed_groups": ["mahum", "isaac"],
   "allowed_role": 5000
}

// User: Mahum
{
   "name": "mahum",
   "role": 5000,
   "groups": ["mahum"]
}

// User: Isaac
{
   "name": "isaac",
   "role": 4000,
   "groups": ["isaac"]
}

// User: Galactor
{
  "name": "galactor",
  "role": 9001,
  "groups": []
}
```

This brick could be accessed by the user `mahum`, because she has the 
role of `5000` and her group is `["mahum"]`. Isaac cannot access this brick 
because although his group includes `isaac` , his role is only `4000` .

Galactor can access whatever they want because their role is `9001`, 
even though they don't have any groups.


## 📚 Useful Links and Resources

 - [FastAPI Documentation](https://fastapi.tiangolo.com/)
 - [FastAPI Tutorial for Beginners](https://fastapi.tiangolo.com/tutorial/)
 - [Postman API Testing Guide](https://www.guru99.com/postman-tutorial.html)
 - [A really good (but advanced) guide to HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
 - [Pydantic Documentation](https://docs.pydantic.dev/latest/)
 - [Git Cheat Sheet PDF](https://education.github.com/git-cheat-sheet-education.pdf)

These resources will help you get started with the tools and technologies used in this workshop.


----------

Thank you @MahumAzeem for the help!


