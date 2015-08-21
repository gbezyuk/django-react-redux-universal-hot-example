import React from 'react';
import {connect} from 'react-redux';
import {loadPage, activatePage} from '../actions/pages';
import {isPageCached} from '../reducers/pages';

@connect(state => ({slug: state.pages.active_page_slug, contents: state.pages.contents_loaded}))
export default class Page extends React.Component {
  static contextTypes = {
    router: React.PropTypes.object.isRequired,
    store: React.PropTypes.object.isRequired
  };

  static fetchData(store, routerParams) {
    const promises = [];
    const slug = routerParams.page_slug;
    promises.push(store.dispatch(
      isPageCached(store.getState(), slug) ? activatePage(slug) : loadPage(slug)
    ));
    return Promise.all(promises);
  }

  render() {
    let content = this.props.contents[this.props.slug];
    return <div className="page" dangerouslySetInnerHTML={{__html: content}} />;
  }
}
