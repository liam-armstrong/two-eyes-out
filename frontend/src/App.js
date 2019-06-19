import React, { Component } from 'react'
import './App.css'
import { connect } from 'react-redux'
import Landing from './components/landing'
import Core from './components/core'
import Nav from './components/nav'

class App extends Component {
  render() {
    return (
      <div className = "container-fluid">
        <Nav />
        { this.props.token == null &&
          <Landing />
        }
        { this.props.token != null &&
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
