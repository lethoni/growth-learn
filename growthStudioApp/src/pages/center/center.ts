import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { Http } from '@angular/http';
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

  constructor(public navCtrl: NavController, public navParams: NavParams, public http: Http, public storage: Storage) {
	this.storage.get('token').then((token:any) => {
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

  ionViewDidLoad() {
    console.log('ionViewDidLoad CenterPage');
  }

}
