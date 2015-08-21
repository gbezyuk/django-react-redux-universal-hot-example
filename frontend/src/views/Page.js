import React from 'react';
import {connect} from 'react-redux';
import {loadPage} from '../actions/pages';

@connect(state => ({content: state.pages.active_page_content}))
export default class Page extends React.Component {
  static contextTypes = {
    router: React.PropTypes.object.isRequired,
    store: React.PropTypes.object.isRequired
  };

  static fetchData(store, routerParams) {
    const promises = [];
    promises.push(store.dispatch(loadPage(routerParams.page_slug)));
    return Promise.all(promises);
  }

  render() {
    return <div className="page" dangerouslySetInnerHTML={{__html: this.props.content}} />;
  }
}
