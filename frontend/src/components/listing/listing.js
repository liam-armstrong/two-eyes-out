import React, { Component } from 'react'
import './listing.css'
import { removeSection, flipActiveSection } from '../../utils/courses';
import { connect } from 'react-redux'

class Listing extends Component {
    constructor(props) {
        super(props)
        this.state = {
          link: ""
        };
      }

    componentDidMount(){
        this.setState({
        link: 'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=' + 
            this.props.listing.section.dept + '&course=' + this.props.listing.section.code + '&section=' + this.props.listing.section.sect
        })
    }

    componentWillReceiveProps(){
        
    }

    remove(){
        removeSection(this.props.listing.section.dept, this.props.listing.section.code, this.props.listing.section.sect)
    }

    flip(){
        flipActiveSection(this.props.listing.section.dept, this.props.listing.section.code, this.props.listing.section.sect)
    }

    render() {
        const activeClass = this.props.listing.active ? "listing" : "listing inactive"
        return (
            <div className = {activeClass}>
                <h2>{this.props.listing.section.dept} {this.props.listing.section.code} {this.props.listing.section.sect}</h2>
                <button onClick={this.flip.bind(this)} style={{marginLeft: 'auto'}} id="power">
                    <i className="material-icons-outlined md-24 md-blue">
                        {this.props.listing.active ? "visibility_off" : "visibility"}
                    </i>
                </button>
                <a href={this.state.link} target="_blank" rel="noopener noreferrer">
                    <i className="material-icons-outlined md-24 md-blue">link</i></a>
                <button onClick={this.remove.bind(this)}>
                    <i className="material-icons-outlined md-24 md-blue">remove_circle_outline</i></button>
            </div>
        );
    }
}

const mapStateToProps = (state, props) => ({
    listing: state.slist.find( listing => { return listing.id === props.id})
});
  
export default connect(mapStateToProps)(Listing);