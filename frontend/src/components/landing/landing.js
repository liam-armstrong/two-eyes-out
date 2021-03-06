import React, { Component } from 'react';
import Login from '../login/login'
import './landing.css'

export default class Landing extends Component {
  render() {
    return (
      <div className = "row">
      <div className="col-md-7" style = {{ paddingLeft: "10vw" }}>
      <h3>Welcome to <b>Two Eyes Out</b>, a seat availability monitoring tool for UBC lectures, labs and tutorials
      <br></br><br></br>Give us a valid section  and course code for any Winter 2019 course and we'll email you once a general seat opens up
      <br></br><br></br>To begin, login or register</h3>
      </div>
      <div className="col-md-5">
           <Login/>
      </div>
  </div>
    );
  }
}