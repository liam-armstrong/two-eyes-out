import axios from 'axios';
import store from '../store';
import { getSections } from '../utils/courses';
import { setToken, setEmail, setError, setSections } from '../actions';
import { URL, LOGIN } from '../config/api';

export function InvalidCredentialsException(message) {
    this.message = message;
    this.name = 'InvalidCredentialsException'
}

export function loginFn(email, password) {
    console.log("POSTING " + email + " + " + password + " to " + URL + LOGIN);
    return axios
        .post(URL + LOGIN, {
            email,
            password
        })
        .then(function (response) {
            store.dispatch(setToken(response.data.token));
            store.dispatch(setEmail(email));
            store.dispatch(setError(false));
            getSections()
        })
        .catch(function (error) {
            console.log("Error in login process");
            console.log("Response status: " + error.status);
            console.log("Response data: " + error.data);
            store.dispatch(setError(true));
            throw new InvalidCredentialsException(error);
        })
        ;
}   

export function loggedIn () {
    return store.getState().token != null;
}

export function logout () {
    store.dispatch(setError(false));    
    store.dispatch(setEmail(null));
    store.dispatch(setSections([]))
    return store.dispatch(setToken(null));
}