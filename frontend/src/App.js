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
<<<<<<< Updated upstream
=======
        }
        { this.props.token != null &&
          <Core />
>>>>>>> Stashed changes
        }
      </div>
    );
  }
}

const mapStateToProps = state => ({
<<<<<<< Updated upstream
  sections: state.sections,
  token: state.token
=======
  token: state.token,
  email: state.email
>>>>>>> Stashed changes
});

export default connect(mapStateToProps)(App);
