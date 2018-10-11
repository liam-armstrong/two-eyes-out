import React, { Component } from 'react';
import { logout }from '../utils/auth'
import './nav.css'

export default class Nav extends Component {
  render() {
    return (
        <nav className = "row">
            <div className = "col-md-2">
              <button><img src="./2eo.png" alt="2eo"></img></button>
            </div>
            { this.props.token !== null &&
              <div className = ".col-md-2 .offset-md-8">
                <button onClick = { logout }>
                  Logout
                </button>
              </div>
            }
        </nav>
    );
  }
}