/*
How to Execute:
1. Open terminal in this project folder.
2. Run: npx expo start
3. Press 'w' for Web or 'a' for Emulator.
*/
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

export default function App() {
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [bmi, setBmi] = useState(null);

  const calculate = () => {
    const w = parseFloat(weight);
    const h = parseFloat(height) / 100;
    if (w > 0 && h > 0) setBmi((w / (h * h)).toFixed(2));
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>BMI Checker</Text>
      <TextInput placeholder="Weight (kg)" onChangeText={setWeight} keyboardType="numeric" style={styles.input} />
      <TextInput placeholder="Height (cm)" onChangeText={setHeight} keyboardType="numeric" style={styles.input} />
      <Button title="Calculate" onPress={calculate} />
      {bmi && <Text style={styles.result}>BMI: {bmi}</Text>}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  input: { borderBottomWidth: 1, width: '80%', marginBottom: 20, padding: 5 },
  result: { marginTop: 20, fontSize: 22, color: 'blue' }
});