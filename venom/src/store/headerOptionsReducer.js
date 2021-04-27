const initialState = {
    headerOptions: {
        options: null
    }
}

const reducer = (state=initialState, action) => {
    switch(action.type) {
        case "UPDATE_OPTIONS":
            const headerOptions = state.headerOptions;
            return {
                ...state,
                headerOptions: {
                    ...headerOptions,
                    options: action.options
                },
            }
        default:
            return state;
    }
};

export default reducer;