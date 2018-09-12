import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

/**
 * Generated class for the BlogListPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-blog-list',
  templateUrl: 'blog-list.html',
})
export class BlogListPage {
  public blogs;
  
  constructor(public navCtrl: NavController, public navParams: NavParams, public http: Http) {
	let url: string = 'http://localhost:8000/api/blog/';
	this.http.get(url)
	  .map(res => res.json())
	  .subscribe(data => {
		this.blogs = data;
	  });
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad BlogListPage');
  }

}
