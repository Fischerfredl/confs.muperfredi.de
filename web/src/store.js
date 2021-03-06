import {
  createStore,
  compose as origCompose,
  applyMiddleware,
  combineReducers
} from 'redux'

import thunk from 'redux-thunk';
import { lazyReducerEnhancer } from 'pwa-helpers/lazy-reducer-enhancer.js'

import app from './reducers/app.js'
import settings from './reducers/settings.js'
import data from './reducers/data.js'

const compose = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || origCompose


const initialState = {
  app: {},
  data: [],
  settings: {}
}

export const store = createStore(
  (state=initialState, action) => state,
  compose(lazyReducerEnhancer(combineReducers), applyMiddleware(thunk))
)

store.addReducers({
  app,
  settings,
  data
})
