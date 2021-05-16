import Dropdown from '../../Dropdown/Dropdown';
import TextInput from '../../TextInput/TextInput';

const Option = (props) => {
    switch(props.type) {
        case "dropdown":
            return (
                <Dropdown title={props.title} options={props.options} key={props.key}
                    multiselect={props.multiselect}
                    onClick={props.onClick}
                    idx={props.idx}
                    selected={props.selected}
                />
            );
        case "textinput":
            return (
                <TextInput title={props.title}
                    value={props.value}
                    onChange={props.onClick}
                    type={props.type}
                    idx={props.idx}
                />
            )
        default:
            return <h1>blah</h1>;
    }
}

export default Option;