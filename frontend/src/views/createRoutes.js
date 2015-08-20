import React from 'react';
import {Route} from 'react-router';
import App from 'views/App';
import Page from 'views/Page';
import Gallery from 'views/Gallery';
import NotFound from 'views/NotFound';

export default function(store) {
  return (
    <Route component={App}>
      <Route path="/page/:page_slug" component={Page}/>
      <Route path="/gallery/:category_slug" component={Gallery}/>
      <Route path="*" component={NotFound}/>
    </Route>
  );
}
