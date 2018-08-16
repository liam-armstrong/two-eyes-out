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
        case actionType.GET_SECTIONS:
            return action.data
        case actionType.UPDATE_SECTION:
            return action.data
        default:
            return state;
    }
}

const appReducer = combineReducers({
    token,
    slist
})

const rootReducer = (state, action) => {
    return appReducer(state, action);
}

export default rootReducer;