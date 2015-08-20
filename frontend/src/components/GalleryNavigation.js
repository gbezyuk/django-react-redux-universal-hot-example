import React, {Component, PropTypes} from 'react';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import {activateCategory, loadCategory} from '../actions/categories';

@connect(
    state => ({categories: state.gallery.categories, active_category_slug: state.gallery.active_category_slug}),
    dispatch => bindActionCreators({activateCategory, loadCategory}, dispatch))

export default class GalleryNavigation extends Component {
  static propTypes = {
    categories: PropTypes.array,
    active_category_slug: PropTypes.string,
    activateCategory: PropTypes.func.isRequired,
    loadCategory: PropTypes.func.isRequired
  }

  activateCategory = (e) => {
    this.props.activateCategory(e.target.dataset.slug);
    this.props.loadCategory(e.target.dataset.id);
    e.preventDefault();
  }

  render() {
    const {categories, active_category_slug} = this.props;
    const styles = require('./Navigation.scss');
    return (
      <div>
        <ul className={styles.navigation + ' ' + styles.gallery}>
          <li className={styles.label}>Gallery Categories:</li>
          {categories.map( (category, i) =>
            <li key={i}><a
              href={'/gallery/' + category.slug}
              className={category.slug == active_category_slug ? styles.active : ''}
              data-id={category.id}
              data-slug={category.slug}
              onClick={this.activateCategory}
              >{category.name}</a></li>
          )}
        </ul>
      </div>
    );
  }
}
