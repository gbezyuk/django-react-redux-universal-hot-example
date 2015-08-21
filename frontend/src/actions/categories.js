import {
  CATEGORIES_LOAD, CATEGORIES_LOAD_SUCCESS, CATEGORIES_LOAD_FAIL,
  CATEGORY_LOAD, CATEGORY_LOAD_SUCCESS, CATEGORY_LOAD_FAIL,
  ACTIVATE_CATEGORY
} from './actionTypes';

export function loadCategories() {
  return {
    types: [CATEGORIES_LOAD, CATEGORIES_LOAD_SUCCESS, CATEGORIES_LOAD_FAIL],
    promise: (client) => client.get('/api/categories.json')
  };
}

export function loadCategory(slug) {
  return {
    types: [CATEGORY_LOAD, CATEGORY_LOAD_SUCCESS, CATEGORY_LOAD_FAIL],
    promise: (client) => client.get(`/api/categories/${slug}.json`)
  };
}


export function activateCategory(slug) {
  return {
    type: ACTIVATE_CATEGORY,
    slug: slug
  };
}
