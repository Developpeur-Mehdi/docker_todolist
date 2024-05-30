db.createUser({
  user: 'admin',
  pwd: 'password',
  roles: [
    {
      role: 'readWrite',
      db: 'todolist'
    }
  ]
});

db.createCollection('todos');

