import Dropdown from '../Dropdown/Dropdown';
import './Style.scss';

const Header = (props) => {
    return (
        <header>
            <div style={{display: 'table-row'}}>
                <Dropdown style={{display: 'table-cell'}} title="Button"/>
                <Dropdown style={{display: 'table-cell'}} title="Another Button"/>
                <Dropdown style={{display: 'table-cell'}} title="ONe MOre Button"/>
            </div>
        </header>
    )
}

export default Header;