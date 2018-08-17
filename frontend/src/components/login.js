import React, { Component } from 'react';
import '../App.css';
import { loginFn } from '../utils/auth';
import './login.css';

export default class Login extends Component {
  constructor(props) {
    super(props)
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.state = {
      email: "",
      password: ""
    };
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  }

  handleSubmit = event => {
    event.preventDefault();
    loginFn(this.state.email, this.state.password)
  }

  render() {
    return (
      <div style={{ height: "200px", width: "300px" }}>
        <form onSubmit={this.handleSubmit}>
          <input 
              id ="email"
              type="email"
              placeholder="email"
              value={this.state.email}
              onChange={this.handleChange}></input><br></br>
          <input
              style = {{ width: "60%"}}
              id="password"
              placeholder="password"
              value={this.state.password}
              onChange={this.handleChange}
              type="password"></input><br></br>
          <button type="submit" style = {{ color : "blue" }}>Login</button><br></br>
          <button href="javascript.void(0);">Register</button>
        </form>
      </div>
    );
  }
}
