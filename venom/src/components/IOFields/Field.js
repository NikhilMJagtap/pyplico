const Field = (props) => {
    return (
        <div className="field">
            <h5 className="field-title">{props.title}</h5>
            <textarea
                value={props.value}
                onChange={e => props.onChange(e.target.value)}
                readOnly={props.readOnly}
            ></textarea>
        </div>
    )
}

export default Field;