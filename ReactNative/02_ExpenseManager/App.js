/*
How to Execute:
1. Open terminal in this project folder.
2. Run: npx expo start
3. Press 'w' for Web or 'a' for Emulator.
*/
import React, { useState } from 'react';
import { View, Text, TextInput, Button, FlatList, StyleSheet } from 'react-native';

export default function App() {
  const [amt, setAmt] = useState('');
  const [list, setList] = useState([]);

  const add = (type) => {
    if(!amt) return;
    setList([{ id: Date.now().toString(), amt, type }, ...list]);
    setAmt('');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Daily Expense Tracker</Text>
      <TextInput placeholder="Amount" value={amt} onChangeText={setAmt} keyboardType="numeric" style={styles.input} />
      <View style={{flexDirection: 'row', gap: 10, marginBottom: 20}}>
        <Button title="+ Income" color="green" onPress={() => add('Income')} />
        <Button title="- Expense" color="red" onPress={() => add('Expense')} />
      </View>
      <FlatList data={list} keyExtractor={item => item.id} renderItem={({ item }) => (
        <Text style={styles.item}>{item.type}: ${item.amt}</Text>
      )} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 50, backgroundColor: '#fff' },
  header: { fontSize: 22, fontWeight: 'bold', marginBottom: 20 },
  input: { borderBottomWidth: 1, marginBottom: 15, padding: 8 },
  item: { padding: 10, borderBottomWidth: 1, borderColor: '#eee' }
});