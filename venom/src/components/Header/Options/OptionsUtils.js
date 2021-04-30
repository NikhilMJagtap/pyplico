import HeaderOptions from '../../../config/HeaderOptions';
import url from '../../../constants/url';

export const getOptionsFromPath = () => {
    const pathname = window.location.pathname;
    switch(pathname) {
        case url.BASE64_DECODE:
            return HeaderOptions.Base64Decode
        default:
            // return ()=>{};
            break;
    }
}

export default getOptionsFromPath;