Domain: Thư viện

1. ERD
   ![ERD](/Week%205/ERD.jpg)

2. Endpoints

- GET /books
- POST /books
- PATCH /books/book_id
- PUT /books/book_id
- DELETE /books/book_id

- GET /publishers
- POST /publishers
- GET /publishers/publisher_id/books
- POST /publishers/publisher_id/books

- GET /users
- POST /users
- PATCH /users/user_id
- PUT /users/user_id
- DELETE /users/user_id

- GET /users/user_id/books
- POST /users/user_id/books

3. JSON Schema cho 3 resources chính
   a. Book
   {
   "type": "object",
   "required": ["id"],
   "properties": {
   "id": {
   "type": "string",
   "format": "uuid"
   }
   "title": {
   "type": "string",
   "minLength": 1,
   "default": ""
   }
   "genre": {
   "type": "string",
   "minLength": 1,
   "default": ""
   }
   "edition": {
   "type": "integer",
   "minimum": 1,
   "default": 1
   }
   "price": {
   "type": "number",
   "minimum": 1,
   "default": 1
   }
   }
   }
   b. Users
   {
   "type": "object",
   "required": ["id"],
   "properties": {
   "id": {
   "type": "string",
   "format": "uuid"
   }
   "name": {
   "type": "string",
   "minLength": 1,
   "default": ""
   }
   }
   }

c. Publishers
{
"type": "object",
"required": ["id"],
"properties": {
"id": {
"type": "string",
"format": "uuid"
}
"name": {
"type": "string",
"minLength": 1,
"default": ""
}
}
}
