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
        { this.props.token == null &&
          <Landing logerror = {this.props.logerror}/>
        }
      </div>
    );
  }
}

const mapStateToProps = state => ({
  sections: state.sections,
  token: state.token,
  email: state.email,
  logerror: state.logerror
});

const mapActionstoProps = {
  handleSubmit: setToken
};

export default connect(mapStateToProps, mapActionstoProps)(App);
