import './Style.scss';

const Modal = (props) => {
    return (
        <div className="modal" style={{display: props.show ? 'block': 'none'}}>
            <div className="modal-content"
                style={{
                    transform: props.show ? 'translateY(0)' : 'translateY(-100vh)',
                    opacity: props.show ? '1': '0'
                }}>
                {props.children}
            </div>
        </div>
    )
}

export default Modal;