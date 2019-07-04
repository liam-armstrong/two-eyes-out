import React, { Component } from 'react'
import Courseform from './courseform'
import { connect } from 'react-redux'
import './core.css'
import Listing from './listing';

class Core extends Component {
  render() {
    return (
      <div className = "container-fluid">
        <div className = "row justify-content-center align-items-center" style = {{height: "30vh"}}>
          <Courseform />
        </div>
        <div className = "row justify-content-center align-items-top listings" style = {{height: "60vh", paddingTop: "5vh"}}>
          <ul className = "justify-content-center">
            {this.props.sections.map((slist) => <li key={slist.id}><Listing id={slist.id} section={slist.section} active={slist.active} premium={slist.premium}/></li>) }
          </ul>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  sections: state.slist
});

export default connect(mapStateToProps)(Core);