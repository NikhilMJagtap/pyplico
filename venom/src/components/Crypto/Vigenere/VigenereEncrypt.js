import { Component, Fragment } from "react";
import Vigenere from "../../../utils/cryptoUtils/Vigenere";
import Header from '../../Header/Header';
import IOFields from "../../IOFields/IOFields";

class VigenereEncrypt extends Component {

    state = {
        inputValue: "",
        outputValue: "",
        errorMessage: "",
        encyrptionKey: "TIMAPPLE",
    }

    onInputChange = (value) => {
        if(value && !value.match(/^[A-Za-z]+$/)) {
            this.setState({
                inputValue: value,
                errorMessage: "Only alphabets allowed in Vigenere Cypher",
            });
            return;
        }
        const encypter = new Vigenere(this.state.encyrptionKey);
        this.setState({
            errorMessage: "",
            inputValue: value,
            outputValue: encypter.encrypt(value),
        })
    }

    render(props) {
        return (
            <Fragment>
                <Header/>
                <div className="workspace">
                    <h3 className="ws-title">Vigenere Encryption</h3>
                    <IOFields
                        onInputChange={this.onInputChange}
                        inputValue={this.state.inputValue}
                        outputValue={this.state.outputValue}
                        outputReadOnly={true}
                    />
                    {
                        this.state.errorMessage ?
                        <p className="error" style={{marginLeft: 10}}>{this.state.errorMessage}</p>
                        : null
                    }
                </div>
            </Fragment>
        )
    }
}

export default VigenereEncrypt;