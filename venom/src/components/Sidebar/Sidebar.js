import {useState, useEffect} from 'react';
import './Style.scss';
import image from '../../assets/venom.png';
import Option from './Option/Option';
import sidebarOptions from '../../config/sidebarOptions'; 
import { connect } from 'react-redux';

const Sidebar = (props) => {
    const [options, setOptions] = useState(sidebarOptions);
    const collapsed = props.sidebarCollapsed;

    useEffect(() => {
        selectedRouteHandler();
        return () => {  
        }
    }, [])

    const onOptionSelectHandler = (name) => {
        let newOptions = [...options];
        for(let i=0; i<options.length; ++i) {
            options[i].selected = false;
            if(options[i].name === name)
                options[i].selected = true;
        }
        setOptions(newOptions);
    }

    const selectedRouteHandler = () => {
        const route = window.location.pathname.indexOf('/', 1) !== -1 ? window.location.pathname.split('/')[1] : "";
        let newOptions = [...options];
        for(let i=0; i<options.length; ++i) {
            if(options[i].name.toLowerCase() === route && options[i].selected) return;
            options[i].selected = false;
            if(options[i].name.toLowerCase() === route)
                options[i].selected = true;
        }
        setOptions(newOptions);
    }

    return (
        <div className={`sidebar ${collapsed ? 'collapsed' : ''}`}>
            <div className="heading">
                <img src={image} className="sidebar-logo"/>
                <div className="sidebar-title">
                    <h4>VƎNOM</h4>
                    <p>Yet Another CTF Tool</p>
                </div>
            </div>
            <div className="divider"></div>
            <div className="options">
                {
                    options.map(x => (
                        <Option key={x.name} 
                            name={x.name} 
                            selected={x.selected}
                            logoURL={x.logoURL} 
                            suboptions={x.suboptions} 
                            onselect={onOptionSelectHandler}
                            collapsed={collapsed}/>
                    ))
                }
            </div>
            <div className="collapse-option">
                <Option name={!collapsed ? "Collapse" : "Expand"}
                    logoURL={"https://www.flaticon.com/svg/static/icons/svg/1665/1665608.svg"}
                    onselect={props.toggleSidebar}
                    collapsed={collapsed}
                />
            </div>
        </div>
    )
}

const mapStateToProps = state => {
    return {
        sidebarCollapsed: state.root.sidebarCollapsed            
    }
}

const mapDispatchToProps = dispatch => {
    return {
        toggleSidebar: () => dispatch({type: 'TOGGLE_SIDEBAR'}),
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Sidebar);

