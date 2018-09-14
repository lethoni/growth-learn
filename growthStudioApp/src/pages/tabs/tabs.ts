import { Component } from '@angular/core';

import { AboutPage } from '../about/about';
import { CenterPage } from '../center/center';
import { HomePage } from '../home/home';
import { BlogListPage } from '../blog-list/blog-list';


@Component({
  templateUrl: 'tabs.html'
})
export class TabsPage {

  tab1Root = HomePage;
  tab2Root = AboutPage;
  tab3Root = CenterPage;
  tab4Root = BlogListPage;

  constructor() {

  }
}
