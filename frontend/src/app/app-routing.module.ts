import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BlogsComponent } from './blogs/blogs.component';
import { BlogDetailComponent } from './blog-detail/blog-detail.component';

const routes: Routes = [
	{ path: '', component: BlogsComponent },
	{ path: 'blog/:id', component: BlogDetailComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
