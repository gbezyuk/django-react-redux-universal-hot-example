import {
  PAGES_LOAD,
  PAGES_LOAD_SUCCESS,
  PAGES_LOAD_FAIL,
  PAGE_LOAD,
  PAGE_LOAD_SUCCESS,
  PAGE_LOAD_FAIL,
  ACTIVATE_PAGE
} from '../actions/actionTypes';

const initialState = {
  pages: {},
  active_page_slug: '',
  loading_pages: false,
  pages_loaded: false,
  loading_page: false,
  page_loaded: false,
  contents_loaded: {}
};

export default function pages(state = initialState, action = {}) {
  switch (action.type) {
    case PAGES_LOAD:
      return {
        ...state,
        loading_pages: true
      };
    case PAGES_LOAD_SUCCESS:
      return {
        ...state,
        loading_pages: false,
        pages_loaded: true,
        pages: action.result
      };
    case PAGES_LOAD_FAIL:
      return {
        ...state,
        loading_pages: false,
        pages_loaded: false,
        error: action.error
      };
    case ACTIVATE_PAGE:
      return {
        ...state,
        active_page_slug: action.slug
      };
    case PAGE_LOAD:
      return {
        ...state,
        loading_page: true
      };
    case PAGE_LOAD_SUCCESS:
      let contents_loaded_updated = {...state.contents_loaded};
      contents_loaded_updated[action.result.slug] = action.result.content;
      return {
        ...state,
        loading_page: false,
        page_loaded: true,
        contents_loaded: contents_loaded_updated,
        active_page_slug: action.result.slug
      };
    case PAGE_LOAD_FAIL:
      return {
        ...state,
        loading_page: false,
        page_loaded: false,
        error: action.error
      };
    default:
      return state;
  }
}

export function arePagesLoaded(globalState) {
  return globalState.pages && globalState.pages.pages_loaded;
}

export function isPageCached(globalState, slug) {
  return globalState.pages && globalState.pages.contents_loaded
    && globalState.pages.contents_loaded[slug];
}
