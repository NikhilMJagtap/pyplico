import { Route, Switch } from 'react-router';
import Base64Encode from '../Crypto/Base64/Base64Encode';
import Base64Decode from '../Crypto/Base64/Base64Decode';
import VigenereEncrypt from '../Crypto/Vigenere/VigenereEncrypt';
import VigenereDecrypt from '../Crypto/Vigenere/VigenereDecrypt';

const Router = (props) => {
    return (
        <Switch>
            <Route path="/pyplico/pcap" exact component={null}/>
            <Route path="/pyplico/dns" exact component={null} />
            <Route path="/crypto/base64-encode" exact component={Base64Encode}/>
            <Route path="/crypto/base64-decode" exact component={Base64Decode}/>
            <Route path="/crypto/vigenere-encode" exact component={VigenereEncrypt} />
            <Route path="/crypto/vigenere-decode" exact component={VigenereDecrypt} />
        </Switch>
    )
}

export default Router;