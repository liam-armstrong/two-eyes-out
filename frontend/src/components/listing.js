import React, { Component } from 'react'
import './listing.css'
import { removeSection, flipActiveSection } from '../utils/courses';

export default class Listing extends Component {
    constructor(props) {
        super(props)
        this.state = {
          className: "listing inactive",
          link: ""
        };
      }

    componentDidMount(){
        this.setState({
        link: 'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=' + 
            this.props.section.dept + '&course=' + this.props.section.code + '&section=' + this.props.section.sect
        })
        if(this.props.active){
            this.setState({
                className: "listing"
            })
        }
    }

    remove(){
        removeSection(this.props.section.dept, this.props.section.code, this.props.section.sect)
    }

    flip(){
        flipActiveSection(this.props.section.dept, this.props.section.code, this.props.section.sect)
    }

    render() {
        return (
            <div className = {this.state.className}>
                <h2>{this.props.section.dept} {this.props.section.code} {this.props.section.sect}</h2>
                <button onClick={this.flip.bind(this)} style={{marginLeft: 'auto'}} id="power"><clr-icon shape="power" size="22" class="is-highlight"></clr-icon></button>
                <a href={this.state.link} target="_blank" rel="noopener noreferrer"><clr-icon shape="link" size="22" class="is-highlight"></clr-icon></a>
                <button onClick={this.remove.bind(this)}><clr-icon shape="times" size="22" class="is-highlight"></clr-icon></button>
            </div>
        );
    }
}