import { Fragment } from 'react';
import { Link, NavLink } from 'react-router-dom';
import './Style.scss';

const Suboption = (props) => {
    return (
        <div className="suboptions">
            {
                props.suboptions.map(x => (
                    <Link key={x} className="suboption" to={'/' + props.option.toLowerCase() + '/' + x.toLowerCase().replace(' ', '-')}>
                        {x}
                    </Link>
                ))
            }
        </div>
    )
}

const Option = (props) => {
    return (
        <Fragment>
            <div className={`option ${props.selected ? 'selected': ''}`} onClick={()=>{props.onselect(props.name)}}>
                <div className="selected-option-mark"></div>
                <img src={props.logoURL}/>
                {props.collapsed ? 
                    <div className="tooltip">{props.name}</div> :
                    <div className="option-text">{props.name}</div>
                }
            </div>
            {
                props.selected && props.suboptions && !props.collapsed? 
                <Suboption suboptions={props.suboptions} option={props.name}/>
                : null
            }
        </Fragment>
    )
}

export default Option;