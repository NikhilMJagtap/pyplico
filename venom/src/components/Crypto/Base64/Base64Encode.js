import { Component, Fragment } from "react";
import Header from '../../Header/Header';
import IOFields from "../../IOFields/IOFields";

class Base64Decode extends Component {
    state = {
        inputValue: "Hello World!",
        outputValue: "SGVsbG8gV29ybGQh="
    }

    onInputChange = (value) => {
        this.setState({
            inputValue: value
        });
        try {
            var decodedValue = window.btoa(value);
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
                    <h3 className="ws-title">Base64 Encoder</h3>
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