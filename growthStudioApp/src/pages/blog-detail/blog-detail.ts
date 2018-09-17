import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

/**
 * Generated class for the BlogDetailPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-blog-detail',
  templateUrl: 'blog-detail.html',
})
export class BlogDetailPage {
  public blog={
	title:'',
	slug:'',
	body:''
  };

  constructor(public navCtrl: NavController, public navParams: NavParams, public http: Http) {
	let blogId = navParams.get("blogId");
	let url = 'http://localhost:8000/api/blog/' + blogId + '/';
	this.http.get(url)
	  .map(res => res.json())
	  .subscribe(data => {
		this.blog = data;
	  });
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad BlogDetailPage');
  }

}
