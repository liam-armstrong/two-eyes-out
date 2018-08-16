import * as actionType from './types';

export const setToken = (data) => {
  return {
    type: actionType.SET_TOKEN,
    data
  }
}

export const getSections = (data) => {
  return {
    type: actionType.GET_SECTIONS,
    data
  }
}

export const updateSection = (data) => {
  return {
    type: actionType.UPDATE_SECTION,
    data
  }
}

export const updateUser = (data) => {
  return {
    type: actionType.UPDATE_USER,
    data
  }
}