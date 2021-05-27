import './Style.scss'

const TextInput = (props) => {
    return (
        <div className="text-input-wrapper">
            <input className="text-input" required 
                value={props.value} 
                type={props.type}
                onChange={(e)=>{
                    props.onChange(props.idx, "textinput", props.key, {value: e.target.value});
                }}
            />
            <div className="text-input-placeholder">{props.title}</div>
        </div>
    )
}

export default TextInput;