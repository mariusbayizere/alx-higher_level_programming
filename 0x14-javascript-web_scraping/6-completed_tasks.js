#!/usr/bin/node

// This script computes the number of tasks completed by user ID.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only users with completed tasks are printed.
// The module 'request' is used to make the HTTP request.

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusCode}`);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId] += 1;
    }
  });

  console.log(completedTasks);
});
