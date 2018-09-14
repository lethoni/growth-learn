import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { Http, Headers, RequestOptions } from '@angular/http';
import 'rxjs/add/operator/map';
import { Storage } from '@ionic/storage';

/**
 * Generated class for the CenterPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-center',
  templateUrl: 'center.html',
})
export class CenterPage {
	public isLogin = false;
	public user = {
	  name:'',
	  password:''
	};
	public blog = {
	  title:'',
	  slug:'',
	  body:''
	};
	public token;
	
  constructor(public navCtrl: NavController, public navParams: NavParams, public http: Http, public storage: Storage) {
	this.storage.get('token').then((token:any) => {
	  this.token = token;
	  if(token){
		this.isLogin = true;
	  }
	});
  }
  
  loginForm(){
	let userInfo = {
	  username:this.user.name,
	  password:this.user.password
	};
	this.http.post("http://localhost:8000/api-token-auth/", userInfo)
	  .map(res => res.json())
	  .subscribe(data => {
		this.isLogin = true;
		this.storage.set('token', data["token"]);
	  });
  }

  logout(){
	this.isLogin = false;
	this.storage.remove('token');
  }
  
  createBlogForm(){
	let blogInfo = {
	  title: this.blog.title,
      author: 1,
      body: this.blog.body,
      slug: this.blog.slug,
	}
	
	let headers = new Headers({'Authorization': 'JWT ' + this.token, 'Content-Type': 'application/json'});
    let options = new RequestOptions({headers:headers});
	
	this.http.post('http://localhost:8000/api/blog/', blogInfo, options)
	  .map(res => res.json())
	  .subscribe(data => {
		console.log(data);
	  });
  }
  
  ionViewDidLoad() {
    console.log('ionViewDidLoad CenterPage');
  }

}
