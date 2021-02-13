
const initialState = {
    sidebarCollapsed: false
};

const reducer = (state=initialState, action) => {
    switch(action.type) {
        case "TOGGLE_SIDEBAR":
            return {
                ...state,
                sidebarCollapsed: !state.sidebarCollapsed,
            }
        default:
            return state;
    }
};

export default reducer;