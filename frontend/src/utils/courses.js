import axios from 'axios';
import store from '../store';
import { setSections, setSLoading } from '../actions'
import { URL, SECTIONS } from '../config/api';
import { loggedIn } from './auth';

function sectionsClient(method, dept, code, sect){
    console.log(method + "ing " + dept + " " + code + " " + sect)
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
        });
}

export function getSections(){
    sectionsClient('get', "", "", "")
}

export async function addSection(dept, code, sect){
    store.dispatch(setSLoading(true))
    await sectionsClient('post', dept, code, sect)
    store.dispatch(setSLoading(false))
}

export function removeSection(dept, code, sect){
    sectionsClient('delete', dept, code, sect)
}

export function flipActiveSection(dept, code, sect){
    sectionsClient('patch', dept, code, sect)
}