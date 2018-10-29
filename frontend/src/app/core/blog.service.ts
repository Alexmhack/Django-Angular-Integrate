import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { Blog } from '../shared/blog';

@Injectable({
  providedIn: 'root'
})
export class BlogService {

  constructor(private http: HttpClient) { }

  private blogsUrl = 'https://evening-falls-50549.herokuapp.com/blogs/api/';

  getBlogs(): Observable<Blog[]> {
  	const url = this.blogsUrl + 'list/';

  	return this.http.get<Blog[]>(url)
  		.pipe(
  			catchError(this.handleError('getBlogs', []))
  		);
  }

  getBlog(id: number): Observable<Blog> {
    const url = this.blogsUrl + `${id}/detail/`;

    return this.http.get<Blog>(url)
      .pipe(
          catchError(this.handleError<Blog>('getBlogs ID=${id}'))
      );
  }


 /**
 * Handle Http operation that failed.
 * Let the app continue.
 * @param operation - name of the operation that failed
 * @param result - optional value to return as the observable result
 */
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      // this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }  
}
