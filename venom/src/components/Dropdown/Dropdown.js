import { Component, Fragment } from "react";
import './Style.scss';
import shevronDown from '../../assets/down-chevron.svg';

class Dropdown extends Component {
    render() {
        return (
            <Fragment>
                <div className="dropdown" style={this.props.style}>
                    <div className="dropdown-title">
                        {this.props.title}
                        {
                            !this.props.multiselect ? 
                            <span>:&nbsp;{this.props.options[this.props.selected].text}</span>
                            : null
                        }
                        <img style={{right: 10, position: 'absolute', height: 10}} src={shevronDown} alt="&#x25BC;" />
                    </div>
                    
                    <div className="dropdown-options">{
                        this.props.options.map(option => {
                            return (
                                <div className="dropdown-option"
                                onClick={()=>{this.props.onClick(
                                    this.props.idx, "dropdown", option.key, 
                                    {
                                        multiselect: this.props.multiselect
                                    }
                                )}}
                                >
                                    {option.text}
                                    {
                                        this.props.multiselect ? 
                                        <input type='checkbox' className="dropdown-option-checkbox"
                                            checked={option.selected}
                                        />
                                        : null
                                    }
                                </div>
                            )
                        })
                    }
                    </div>
                </div>
            </Fragment>
        )
    }
}

export default Dropdown;