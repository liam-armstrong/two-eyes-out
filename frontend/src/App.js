import React, { Component } from 'react';
import './App.css';
import { setToken } from './actions/index'
import { connect } from 'react-redux';
import Landing from './components/landing'
import Nav from './components/nav'

class App extends Component {
  render() {
    return (
      <div className = "container-fluid">
        <Nav />
        <Landing />
        {this.props.token !== null &&
          <span>{ this.props.token }</span>
        }
      </div>
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
