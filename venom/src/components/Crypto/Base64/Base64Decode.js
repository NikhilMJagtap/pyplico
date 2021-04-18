import { Component, Fragment } from "react";
import Header from '../../Header/Header';
import IOFields from "../../IOFields/IOFields";

class Base64Decode extends Component {
    state = {
        inputValue: "SGVsbG8gV29ybGQh=",
        outputValue: "Hello World!"
    }

    onInputChange = (value) => {
        this.setState({
            inputValue: value
        });
        while(value.indexOf('"') !== -1)
            value = value.replace('"', '');
        try {
            var decodedValue = window.atob(value);
        } catch {
            
        }
        
        this.setState({
            outputValue: decodedValue
        })
    }

    onOutputChange = (value) => {
        console.log(value);
    }
    render() {
        return (
            <Fragment>
                <Header/>
                <div className="workspace">
                    <h3 className="ws-title">Base64 Decoder</h3>
                    <IOFields
                        onInputChange={this.onInputChange}
                        inputValue={this.state.inputValue}
                        outputValue={this.state.outputValue}
                        onOutputChange={this.onOutputChange}
                        outputReadOnly={true}
                    />
                </div>
            </Fragment>
        )
    }
}

export default Base64Decode;