const HeaderOptions = {
    Base64Decode: {
        options: [
            {
                title: "Decode Method",
                key: "decode_method",
                options: [
                    {"text": "Single Shot", "key": "single", "selected": true},
                    {"text": "Recursive", "key": "recursive", "selected": false},
                    {"text": "Match Regex", "key": "regex", "selected": false}
                ],
                type: "dropdown",
                multiselect: false,
                selected: 0
            },
            {
                title: "No. of Rounds",
                key: "rounds",
                type: "textinput",
                value: 1,
            },
            {
                title: "Match RegEx",
                key: "regex",
                type: "textinput",
                value: "",
            }
        ]
    }
}

export default HeaderOptions;