import React, {Component, PropTypes} from 'react';
import {Link} from 'react-router';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import DocumentMeta from 'react-document-meta';
import {createTransitionHook} from '../universalRouter';
import FAQ from '../components/FAQ';
import {arePagesLoaded} from '../reducers/pages';
import {areCategoriesLoaded} from '../reducers/gallery';
import {loadPages} from '../actions/pages';
import {loadCategories} from '../actions/categories';
import PagesNavigation from '../components/PagesNavigation';
import GalleryNavigation from '../components/GalleryNavigation';

const title = 'Django React Redux Example';
const description = 'All the modern best practices in one example — now with Django backend included';
const image = 'https://react-redux.herokuapp.com/logo.jpg';

const meta = {
  title,
  description,
  meta: {
    charSet: 'utf-8',
    property: {
      'og:site_name': title,
      'og:image': image,
      'og:locale': 'en_US',
      'og:title': title,
      'og:description': description,
      'twitter:card': 'summary',
      'twitter:site': '@erikras',
      'twitter:creator': '@erikras',
      'twitter:title': title,
      'twitter:description': description,
      'twitter:image': image,
      'twitter:image:width': '200',
      'twitter:image:height': '200'
    }
  }
};

// @connect(
//     state => ({user: state.auth.user}),
//     dispatch => bindActionCreators({logout}, dispatch))
export default class App extends Component {
  static contextTypes = {
    router: PropTypes.object.isRequired,
    store: PropTypes.object.isRequired
  };

  static fetchData(store) {
    const promises = [];
    if (!arePagesLoaded(store.getState())) {
      promises.push(store.dispatch(loadPages()));
    }
    if (!areCategoriesLoaded(store.getState())) {
      promises.push(store.dispatch(loadCategories()));
    }
    return Promise.all(promises);
  }

  componentWillMount() {
    const {router, store} = this.context;
    this.transitionHook = createTransitionHook(store);
    router.addTransitionHook(this.transitionHook);
  }

  componentWillUnmount() {
    const {router} = this.context;
    router.removeTransitionHook(this.transitionHook);
  }

  // componentWillReceiveProps(nextProps) {
  //   if (!this.props.user && nextProps.user) {
  //     // login
  //     this.context.router.transitionTo('/loginSuccess');
  //   } else if (this.props.user && !nextProps.user) {
  //     // logout
  //     this.context.router.transitionTo('/');
  //   }
  // }

  // handleLogout(event) {
  //   event.preventDefault();
  //   this.props.logout();
  // }

  render() {
    // const {user} = this.props;
    const styles = require('./App.scss');
    return (
      <div className={styles.app}>
        <PagesNavigation />
        <GalleryNavigation />
        <DocumentMeta {...meta}/>
        <div className={styles.content}>
          {this.props.children}
        </div>
        <FAQ />
      </div>
    );
  }
}
