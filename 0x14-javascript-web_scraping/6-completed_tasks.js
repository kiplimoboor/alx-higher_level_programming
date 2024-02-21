#!/usr/bin/node

/*
 * Gets number of Todos a User has completed
 */

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    return;
  }
  const todos = JSON.parse(body);
  const completedTodos = {};
  for (const todo of todos) {
    const userId = todo.userId.toString();
    if (todo.completed) {
      completedTodos[userId] = (completedTodos[userId] ?? 0) + 1;
    }
  }
  console.log(completedTodos);
});
