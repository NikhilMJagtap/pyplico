import Option from './Option';
import { connect } from 'react-redux';
import getOptionsFromPath from './OptionsUtils';


const OptionsWrapper = (props) => {

    const optionsClickHandler = (idx, type, key, data) => {
        let options = [...props.options.options];
        let option = options[idx];
        switch(type) {
            case "dropdown":
                option.options.map((op, i) => {
                    if(op.key === key) {
                        if (data.multiselect) {
                            op.selected = !op.selected;
                        } else {
                            option.selected = i;
                        }
                    }
                })
                break;
            default:
                console.log(idx, type, key, data);
        }
        options[idx] = option;
        props.updateOptions(options);
    }

    return (
        <div style={{display: 'flex', alignItems: 'center', height: '90%', gap: '10px'}} >
            {
                props.options.options.map((op, idx) => (
                    <Option 
                        title={op.title}
                        options={op.options}
                        type={op.type}
                        key={op.key}
                        multiselect={op.multiselect}
                        onClick={optionsClickHandler}
                        idx={idx}
                        selected={op.selected}
                    />
                ))
            }
        </div>
    )
}

const mapStateToProps = state => {
    return {
        options: state.header.headerOptions.options ? state.header.headerOptions : getOptionsFromPath()          
    }
}

const mapDispatchToProps = dispatch => {
    return {
        updateOptions: (options) => dispatch({type: 'UPDATE_OPTIONS', options: options}),
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(OptionsWrapper);