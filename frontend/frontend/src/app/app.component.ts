import { Component, OnInit } from '@angular/core';
import { TodoService } from './todo.service';
import { Todo } from './todo.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  todos: Todo[] = [];
  newTodoContent = '';

  constructor(private todoService: TodoService) {}

  ngOnInit(): void {
    this.loadTodos();
  }

  loadTodos(): void {
    this.todoService.getTodos().subscribe(todos => {
      this.todos = todos;
    });
  }

  addTodo(): void {
    const newTodo: Todo = { content: this.newTodoContent };
    this.todoService.addTodo(newTodo).subscribe(todo => {
      this.todos.push(todo);
      this.newTodoContent = '';
    });
  }

  deleteTodo(_id?: string): void {
    if (_id) {
      this.todoService.deleteTodo(_id).subscribe(() => {
        this.todos = this.todos.filter(todo => todo._id !== _id);
      });
    }
  }
}
