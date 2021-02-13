import {Fragment} from 'react';
import './Style.scss';

const layout = (props) => (
    <Fragment>
        <div>
            Toolbar, Sidedrawer, Backdrop
        </div>
        <main className="content">
            { props.children }
        </main>
    </Fragment>
)

export default layout