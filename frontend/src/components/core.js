import React, { Component } from 'react'
import Courseform from './courseform'
import './core.css'

export default class Core extends Component {
  render() {
    return (
      <div className = "container-fluid">
        <div className = "row justify-content-center align-items-center" style = {{height: "30vh"}}>
          <Courseform />
        </div>
        <div className = "row justify-content-center align-items-center" style = {{height: "60vh"}}>
          <h1>Liam Time</h1>
        </div>
      </div>
    );
  }
}