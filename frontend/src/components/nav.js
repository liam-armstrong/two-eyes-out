import React, { Component } from 'react';
import { logout }from '../utils/auth'
import './nav.css'

export default class Nav extends Component {
  render() {
    return (
        <nav className = "row">
            <div className = "col-md-2">
              <button><img src="./2eo.png"></img></button>
            </div>
            if () {
              <div className = ".col-md-2 .offset-md-8">
                <button onClick = { logout }>
                  Log out
                </button>
              </div>
            }
        </nav>
    );
  }
}