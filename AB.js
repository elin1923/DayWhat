import React from 'react';
import {Text, View} from 'react-native';

var customData = require('./newJson.json')
var d = new Date(2018, 3, 16)

export default class AB extends React.Component {
    render() {
        return (
            <View>
                <Text style={{fontSize: 72}}>{customData[d.toISOString().slice(0, 10)]}</Text>
            </View>
        )
    }
}
