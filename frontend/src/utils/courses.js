import axios from 'axios';
import store from '../store';
import { setSections } from '../actions'
import { URL, SECTIONS } from '../config/api';
import { loggedIn } from './auth';

function sectionsClient(method, dept, code, sect){
    if(!loggedIn()){
        throw Error('Error: "User is not logged in"')
    }
    return axios({
            method: method,
            headers: {'Authorization': 'JWT ' + store.getState().token},
            url: URL + SECTIONS,
            data: {
                'dept': dept,
                'code': code,
                'sect': sect
            }
        })
        .then(function (response) {
            console.log("Status: " + response.status);
            store.dispatch(setSections(response.data));
            console.log(store.getState().slist);
        })
        .catch(function (error) {
            console.log(error);
            throw error
        })
        ;
}

export function getSections(){
    sectionsClient('get', "", "", "")
}

export function addSection(dept, code, sect){
    sectionsClient('post', dept, code, sect)
}

export function removeSection(dept, code, sect){
    sectionsClient('delete', dept, code, sect)
}

export function flipActiveSection(dept, code, sect){
    sectionsClient('update', dept, code, sect)
}