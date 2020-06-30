import React, { Component } from 'react'
import Courseform from '../courseform/courseform'
import { connect } from 'react-redux'
import { WaveTopBottomLoading  } from "react-loadingg";

import './core.css'
import Listing from '../listing/listing';

class Core extends Component {
  render() {
    return (
      <div className = "container-fluid">
        <div className = "row justify-content-center align-items-center" style = {{height: "10vh"}}>
          { this.props.loading &&
            <div className = "justify-content-center align-items-center" style = {{display: "flex", "flex-direction": "column"}}>
              <WaveTopBottomLoading 
              size="large"
              color="#ffcc7f"
              style = {{position: "relative"}}
              />
              <p>Getting Class Data...</p>
            </div>
          }
        </div>
        <div className = "row justify-content-center align-items-center" style = {{height: "20vh"}}>
          <Courseform />
        </div>
        <div className = "row justify-content-center align-items-top listings" style = {{height: "60vh", paddingTop: "5vh"}}>
          <ul className = "justify-content-center">
            {this.props.sections.map((slist) => <li key={slist.id}><Listing id={slist.id}/></li>) }
          </ul>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  sections: state.slist,
  loading: state.sectionLoading
});

export default connect(mapStateToProps)(Core);