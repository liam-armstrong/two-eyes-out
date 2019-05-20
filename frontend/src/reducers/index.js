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

const appReducer = combineReducers({
    token,
    slist,
    email
})

const rootReducer = (state, action) => {
    return appReducer(state, action);
}

export default rootReducer;