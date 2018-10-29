import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { Blog } from '../shared/blog';
import { BlogService } from '../core/blog.service';

@Component({
  selector: 'app-blog-detail',
  templateUrl: './blog-detail.component.html',
  styleUrls: ['./blog-detail.component.scss']
})
export class BlogDetailComponent implements OnInit {

  constructor(
  	private blogService: BlogService,
  	private route: ActivatedRoute,
  	private location: Location
  ) { }

  blog: Blog;

  ngOnInit() {
  	this.getBlog();
  }

  getBlog() {
  	const id = +this.route.snapshot.paramMap.get('id')
  	this.blogService.getBlog(id)
  		.subscribe(blog => this.blog = blog)
  }

  goBack(): void {
  	this.location.back();
  }

}
