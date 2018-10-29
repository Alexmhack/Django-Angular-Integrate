import { Component, OnInit } from '@angular/core';

import { Blog } from '../shared/blog';
import { BlogService } from '../core/blog.service';

@Component({
  selector: 'app-blogs',
  templateUrl: './blogs.component.html',
  styleUrls: ['./blogs.component.scss']
})
export class BlogsComponent implements OnInit {

  constructor(private blogService: BlogService) { }

  blogs: Blog[] = [];

  ngOnInit() {
  	this.getBlogs();
  }

  getBlogs(): void {
  	this.blogService.getBlogs()
  		.subscribe(blogs => this.blogs = blogs);
  }

}
