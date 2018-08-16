import React, { Component } from 'react';
import '../App.css';
import { loginFn } from '../utils/auth'

export default class login extends Component {
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
      <login>
        <form onSubmit={this.handleSubmit}>
          <input 
              id ="email"
              autoFocus
              type="email"
              value={this.state.email}
              onChange={this.handleChange}></input><br></br>
          <input 
              id="password"
              value={this.state.password}
              onChange={this.handleChange}
              type="password"></input><br></br>
          <button type="submit">Login</button>
        </form>
      </login>
    );
  }
}
