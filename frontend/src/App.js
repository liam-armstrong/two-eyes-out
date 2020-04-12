import React, { Component } from 'react'
import './App.css'
import { connect } from 'react-redux'
import Landing from './components/landing/landing.js'
import Core from './components/core/core.js'
import Nav from './components/nav/nav.js'
import { loggedIn } from './utils/auth.js';

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
  token: state.token
});

export default connect(mapStateToProps)(App);
