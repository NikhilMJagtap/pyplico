import './Style.scss';
import Router from '../Router/Router';
import { connect } from 'react-redux';

const Workspace = (props) => {
    return (
        <div className={`workspace-wrapper ${props.sidebarCollapsed ? 'collapsed' : ''}`} >
            <div>
                <Router/>
            </div>
        </div>
    )
}

const mapStateToProps = state => {
    return {
        sidebarCollapsed: state.root.sidebarCollapsed            
    }
}

export default connect(mapStateToProps)(Workspace);