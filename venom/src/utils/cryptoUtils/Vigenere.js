export default class Vigenere {

    constructor(keyword) {
        this.keyword = keyword.toUpperCase();
    }

    generateKey(size) {
        let key = "";
        const fullKeywords = Math.floor(size/this.keyword.length);
        for(let i=0; i<fullKeywords; ++i)
            key += this.keyword;
        for(let i=0; i<size%this.keyword.length; ++i)
            key += this.keyword[i];
        return key;
    }

    encrypt(plainText) {
        return this.encryptionHelper(plainText.toUpperCase());    
    }

    encryptionHelper(plainText) {
        let cypherText = "";
        const key = this.generateKey(plainText.length);
        for(let i=0; i<plainText.length; ++i)
            cypherText += String.fromCharCode((plainText[i].charCodeAt() + key[i].charCodeAt()) % 26 + 65);
        return cypherText;
    }

    decrypt(cypherText) {
        return this.decryptionHelper(cypherText);
    }

    decryptionHelper(cypherText) {
        let plainText = "";
        const key = this.generateKey(cypherText.length);
        for(let i=0; i<cypherText.length; ++i) 
            plainText += String.fromCharCode((cypherText[i].charCodeAt() - key[i].charCodeAt() + 26) % 26 + 65);
        return plainText;
    }

}