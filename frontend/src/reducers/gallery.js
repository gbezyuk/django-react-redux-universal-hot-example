import {
  CATEGORIES_LOAD,
  CATEGORIES_LOAD_SUCCESS,
  CATEGORIES_LOAD_FAIL,
  CATEGORY_LOAD,
  CATEGORY_LOAD_SUCCESS,
  CATEGORY_LOAD_FAIL,
  ACTIVATE_CATEGORY,
  ACTIVATE_PHOTO
} from '../actions/actionTypes';

const initialState = {
  categories: {},
  active_category_slug: '',
  active_category_photos: {},
  active_photo_slug: '',
  loading_categories: false,
  categories_loaded: false,
  loading_category: false,
  category_loaded: false
};

export default function categories(state = initialState, action = {}) {
  switch (action.type) {
    case CATEGORIES_LOAD:
      return {
        ...state,
        loading_categories: true
      };
    case CATEGORIES_LOAD_SUCCESS:
      return {
        ...state,
        loading_categories: false,
        categories_loaded: true,
        categories: action.result
      };
    case CATEGORIES_LOAD_FAIL:
      return {
        ...state,
        loading_categories: false,
        categories_loaded: false,
        error: action.error
      };
    case ACTIVATE_CATEGORY:
      return {
        ...state,
        active_category_slug: action.slug
      }
    case CATEGORY_LOAD:
      return {
        ...state,
        loading_category: true
      };
    case CATEGORY_LOAD_SUCCESS:
      return {
        ...state,
        loading_category: false,
        category_loaded: true,
        active_category_photos: action.result.photos,
        active_category_slug: action.result.slug
      };
    case CATEGORY_LOAD_FAIL:
      return {
        ...state,
        loading_category: false,
        category_loaded: false,
        error: action.error
      };
    case ACTIVATE_PHOTO:
      return {
        ...state,
        active_photo_slug: action.slug
      }
    default:
      return state;
  }
}

export function areCategoriesLoaded(globalState) {
  return globalState.gallery && globalState.gallery.categories_loaded;
}
