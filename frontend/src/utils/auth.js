import axios from 'axios';
import _ from 'lodash';
import store from '../store';
import { getSections } from '../utils/courses';
import { setToken, setEmail, setError } from '../actions';
import { URL, LOGIN } from '../config/api';

export function InvalidCredentialsException(message) {
    this.message = message;
    this.name = 'InvalidCredentialsException'
}

export function loginFn(email, password) {
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
            console.log(error);
            store.dispatch(setError(true));
            throw new InvalidCredentialsException(error);
        })
        ;
}   

export function loggedIn () {
    return store.getState().token != null;
}

export function logout () {
    store.dispatch(setEmail(null));
    return store.dispatch(setToken(null));
}