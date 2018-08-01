import axios from 'axios';
import _ from 'lodash';
import store from '../store';
import { setToken } from '../actions';
import { URL, LOGIN } from '../config/Api';

export function InvalidCredentialsException(message) {
    this.message = message;
    this.name = 'InvalidCredentialsException'
}

export function login(email, password) {
    return axios
        .post(URL + LOGIN, {
            email,
            password
        })
        .then(function (response) {
            store.dispatch(setToken(response.data.token));
        })
        .catch(function (error) {
            //if error due to invalid credentials raise different error
            if (_.get(error, 'response.status') === 400) {
                throw new InvalidCredentialsException(error);
            }
            throw error;
        });
}   

export function loggedIn () {
    return store.getState().token == null;
}