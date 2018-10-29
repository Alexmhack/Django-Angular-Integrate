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
  blog: Blog;

  ngOnInit() {
  	this.getBlogs();
  }

  getBlogs(): void {
  	this.blogService.getBlogs()
  		.subscribe(blogs => this.blogs = blogs);
  }

  getBlog(id: number): void {
    this.blogService.getBlog(id)
      .subscribe(blog => this.blog = blog);
  }

}
