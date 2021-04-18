import { Component } from "react";
import Field from "./Field";
import './Style.scss';

class IOFields extends Component {
    render() {
        return (
            <div className="iofields sided">
                <Field title="Input" 
                    value={this.props.inputValue} 
                    onChange={this.props.onInputChange}
                />
                <Field title="Output" 
                    value={this.props.outputValue} 
                    onChange={this.props.onOutputChange}
                    readOnly={this.props.outputReadOnly} 
                />
            </div>
        )
    }
}

export default IOFields;