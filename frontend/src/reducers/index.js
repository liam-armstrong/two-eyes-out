import { combineReducers } from 'redux';
import * as actionType from '../actions/types'

//Token initial state and reducer
const tokenInitialState = null;
const token = (state = tokenInitialState, action) => {
    switch(action.type) {
        case actionType.SET_TOKEN:
            return action.data
        default:
            return state;
    }
}

//Section list initial state and reducer
const slistInitialState = [];
const slist = (state = slistInitialState, action) => {
    switch(action.type) {
        case actionType.SET_SECTIONS:
            return action.data
        default:
            return state;
    }
}

//Email initial state and reducer
const emailInitialState = null;
const email = (state = emailInitialState, action) => {
    switch(action.type) {
        case actionType.SET_EMAIL:
            return action.data
        default:
            return state;
    }
}

//Login Error initial state and reducer
const logerrorInitialState = false;
const logerror = (state = logerrorInitialState, action) => {
    switch(action.type) {
        case actionType.SET_ERROR:
            return action.data
        default:
            return state;
    }
}

const sectionLoadingInit = false;
const sectionLoading = (state = sectionLoadingInit, action) => {
    switch(action.type) {
        case actionType.SET_SLOADING:
            return action.data
        default:
            return state;
    }
}

const appReducer = combineReducers({
    token,
    slist,
    email,
    logerror,
    sectionLoading
})

const rootReducer = (state, action) => {
    return appReducer(state, action);
}

export default rootReducer;