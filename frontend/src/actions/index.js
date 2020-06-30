import * as actionType from './types';

export const setToken = (data) => {
  return {
    type: actionType.SET_TOKEN,
    data
  }
}

export const setEmail = (data) => {
  return {
    type: actionType.SET_EMAIL,
    data
  }
}

export const setSections = (data) => {
  return {
    type: actionType.SET_SECTIONS,
    data
  }
}

export const setError = (data) => {
  return {
    type: actionType.SET_ERROR,
    data
  }
}

export const setSLoading = (data) => {
  return {
    type: actionType.SET_SLOADING,
    data
  }
}
