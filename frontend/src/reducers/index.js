import {createFormReducer} from 'redux-form';
export pages from './pages';
export gallery from './gallery';
export auth from './auth';
export const survey = createFormReducer('survey', ['name', 'email', 'occupation']);
