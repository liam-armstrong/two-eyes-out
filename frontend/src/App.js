import React, { Component } from 'react';
import './App.css';
import { setToken } from './actions/index'
import { connect } from 'react-redux';
import login from './components/login.jsx'

class App extends Component {
  render() {
    return (
      <login />,
      <h1>login</h1>
    );
  }
}

const mapStateToProps = state => ({
  sections: state.sections,
  token: state.token
});

const mapActionstoProps = {
  handleSubmit: setToken
};

export default connect(mapStateToProps, mapActionstoProps)(App);
