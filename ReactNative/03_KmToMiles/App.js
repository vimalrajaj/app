import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';

export default function App() {
  const [km, setKm] = useState('');
  const [mi, setMi] = useState('');

  return (
    <View style={{ padding: 50, alignItems: 'center' }}>
      <Text style={{fontSize: 22, fontWeight: 'bold', marginBottom: 20}}>Km to Miles</Text>
      <TextInput placeholder="Enter Kilometers" onChangeText={setKm} keyboardType="numeric" style={{borderBottomWidth: 1, width: '100%', marginBottom: 20}} />
      <Button title="Convert to Miles" onPress={() => setMi((km * 0.621371).toFixed(2))} />
      <Text style={{fontSize: 24, marginTop: 40}}>Result: {mi} Miles</Text>
    </View>
  );
}