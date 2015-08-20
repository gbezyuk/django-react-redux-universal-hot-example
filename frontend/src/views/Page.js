import React from 'react';
import {connect} from 'react-redux';

@connect(state => ({content: state.pages.active_page_content}))
export default class Page extends React.Component {
  static contextTypes = {
    router: React.PropTypes.object.isRequired,
    store: React.PropTypes.object.isRequired
  };

  static fetchData(store) {
    const promises = [];
    let page_slug = this.context.router.getParams().page_slug;
    console.log(page_slug);
    if (!isPageLoaded(store.getState())) {
      promises.push(store.dispatch(loadPage(page_slug)));
    }
    return Promise.all(promises);
  }

  render() {
    return <div className="page" dangerouslySetInnerHTML={{__html: this.props.content}} />;
  }
}
