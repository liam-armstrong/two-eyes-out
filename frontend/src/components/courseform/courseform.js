import React, { Component } from 'react';
import '../login/login.css';
import { addSection } from '../../utils/courses';

export default class Courseform extends Component {
  constructor(props) {
    super(props)
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.state = {
      dept: "",
      code: "",
      sect: ""
    };
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  }

  handleSubmit = event => {
    event.preventDefault();
    addSection(this.state.dept, this.state.code, this.state.sect)
  }

  render() {
    return (
      <div className="row">
        <form onSubmit={this.handleSubmit} className="inline-form">
            <input 
                id ="dept"
                type="dept"
                placeholder="ex CPSC"
                value={this.state.dept}
                onChange={this.handleChange}></input>
            <input
                id="code"
                placeholder="ex 110"
                value={this.state.code}
                onChange={this.handleChange}></input> 
            <input
                id="sect"
                placeholder="ex 102"
                value={this.state.sect}
                onChange={this.handleChange}></input> 
          <button type="submit" style = {{ color : "blue"}}>Add</button>
        </form>
      </div>
    );
  }
}

