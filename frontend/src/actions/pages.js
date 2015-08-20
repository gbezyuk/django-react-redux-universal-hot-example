import {
  PAGES_LOAD, PAGES_LOAD_SUCCESS, PAGES_LOAD_FAIL,
  PAGE_LOAD, PAGE_LOAD_SUCCESS, PAGE_LOAD_FAIL,
  ACTIVATE_PAGE
} from './actionTypes';

export function loadPages() {
  return {
    types: [PAGES_LOAD, PAGES_LOAD_SUCCESS, PAGES_LOAD_FAIL],
    promise: (client) => client.get('/api/pages.json')
  };
}

export function loadPage(slug) {
  return {
    types: [PAGE_LOAD, PAGE_LOAD_SUCCESS, PAGE_LOAD_FAIL],
    promise: (client) => client.get(`/pages/${slug}.json`)
  };
}


export function activatePage(slug) {
  return {
    type: ACTIVATE_PAGE,
    slug: slug
  };
}
