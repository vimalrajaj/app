/*
How to Execute:
1. Open terminal in this project folder.
2. Run: npx expo start
3. Press 'w' for Web or 'a' for Emulator.
*/
import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';

export default function App() {
  const [kg, setKg] = useState('');
  const [lbs, setLbs] = useState('');

  return (
    <View style={{ padding: 50, alignItems: 'center' }}>
      <Text style={{fontSize: 22, fontWeight: 'bold', marginBottom: 20}}>Kg to Pounds</Text>
      <TextInput placeholder="Enter Kilograms" onChangeText={setKg} keyboardType="numeric" style={{borderBottomWidth: 1, width: '100%', marginBottom: 20}} />
      <Button title="Convert to Pounds" onPress={() => setLbs((kg * 2.20462).toFixed(2))} />
      <Text style={{fontSize: 24, marginTop: 40}}>Result: {lbs} Lbs</Text>
    </View>
  );
}