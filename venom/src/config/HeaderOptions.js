const HeaderOptions = {
    Base64Decode: {
        options: [
            {
                title: "Decode Method",
                key: "decode_method",
                options: [
                    {"text": "Single Shot", "key": "single", "selected": true},
                    {"text": "Recursive", "key": "recursive", "selected": false}
                ],
                type: "dropdown",
                multiselect: false,
                selected: 0
            },
            {
                title: "Character Set",
                key: "char_set",
                options: [
                    {"text": "UTF-8", "key": "utf", "selected": true},
                    {"text": "ASCII", "key": "ascii", "selected": false}
                ],
                type: "dropdown",
                multiselect: true
            }
        ]
    }
}

export default HeaderOptions;