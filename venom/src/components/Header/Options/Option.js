import Dropdown from '../../Dropdown/Dropdown';

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
        default:
            return <h1>blah</h1>;
    }
}

export default Option;