import React, { Component } from 'react'
import './App.css'
import { connect } from 'react-redux'
import Landing from './components/landing'
import Core from './components/core'
import Nav from './components/nav'
import { loggedIn } from './utils/auth';

class App extends Component {
  render() {
    return (
      <div className = "container-fluid">
        <Nav />
        { !loggedIn() &&
          <Landing />
        }
        { loggedIn() &&
          <Core />
        }
      </div>
    );
  }
}

const mapStateToProps = state => ({
  sections: state.sections,
  token: state.token,
  email: state.email
});

export default connect(mapStateToProps)(App);
