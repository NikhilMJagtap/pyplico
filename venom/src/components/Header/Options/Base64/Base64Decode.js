import Option from '../Option';

const Base64Decode = (props) => {
    return (
        <div style={{display: 'flex', alignItems: 'center', height: '90%', gap: '10px'}} >
            {
                props.options.options.map(op => (
                    <Option 
                        title={op.title}
                        options={op.options}
                        type={op.type}
                        key={op.key}
                    />
                ))
            }
        </div>
    )
}


export default Base64Decode;