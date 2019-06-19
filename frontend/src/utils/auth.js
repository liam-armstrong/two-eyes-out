import axios from 'axios';
import _ from 'lodash';
import store from '../store';
import { setToken, setEmail, setError } from '../actions';
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
            console.log("Status: " + response.status);
            store.dispatch(setToken(response.data.token));
            store.dispatch(setEmail(email));
            store.dispatch(setError(false));
        })
        .catch(function (error) {
            console.log(error);
            store.dispatch(setError(true));
            throw new InvalidCredentialsException(error);
            //if error due to invalid credentials raise different error
            // if (_.get(error, 'response.status') === 400) {
            //     throw new InvalidCredentialsException(error);
            // }
            // throw error;
        })
        ;
}   

export function loggedIn () {
    return store.getState().token == null;
}

export function logout () {
    store.dispatch(setEmail(null));
    return store.dispatch(setToken(null));
}