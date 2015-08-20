import React, {Component, PropTypes} from 'react';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import {activatePage, loadPage} from '../actions/pages';

@connect(
    state => ({pages: state.pages.pages, active_page_slug: state.pages.active_page_slug}),
    dispatch => bindActionCreators({activatePage, loadPage}, dispatch))

export default class PagesNavigation extends Component {
  static propTypes = {
    pages: PropTypes.array,
    active_page_slug: PropTypes.string,
    activatePage: PropTypes.func.isRequired,
    loadPage: PropTypes.func.isRequired
  }

  static contextTypes = {
    router: PropTypes.object.isRequired,
    store: PropTypes.object.isRequired
  };

  activateAndLoadPage = (e) => {
    e.preventDefault();
    let slug = e.target.dataset.slug;
    this.props.activatePage(slug);
    this.props.loadPage(slug);
    this.context.router.transitionTo('/page/' + slug);
  }

  render() {
    const {pages, active_page_slug} = this.props;
    const styles = require('./Navigation.scss');
    return (
      <div>
        <ul className={styles.navigation + ' ' + styles.pages}>
          <li className={styles.label}>Pages:</li>
          {pages.map( (page, i) =>
            <li key={i}><a
              href={'/page/' + page.slug}
              className={page.slug == active_page_slug ? styles.active : ''}
              data-slug={page.slug}
              onClick={this.activateAndLoadPage}
              >{page.name}</a></li>
          )}
        </ul>
      </div>
    );
  }
}
