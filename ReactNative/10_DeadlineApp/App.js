/*
How to Execute:
1. Open terminal in this project folder.
2. Run: npx expo start
3. Press 'w' for Web or 'a' for Emulator.
*/
import React, { useState } from 'react';
import { View, Text, TextInput, Button, FlatList, StyleSheet } from 'react-native';

export default function App() {
  const [task, setTask] = useState('');
  const [due, setDue] = useState('');
  const [list, setList] = useState([]);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Task Deadlines</Text>
      <TextInput placeholder="Task Name" onChangeText={setTask} style={styles.input} />
      <TextInput placeholder="Deadline Time" onChangeText={setDue} style={styles.input} />
      <Button title="Save Deadline" onPress={() => setList([{task, due, id: Date.now().toString()}, ...list])} />
      <FlatList data={list} keyExtractor={item => item.id} renderItem={({item}) => (
        <View style={styles.item}><Text>• {item.task} - Due: {item.due}</Text></View>
      )} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 50, flex: 1 },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 20 },
  input: { borderBottomWidth: 1, marginBottom: 15, padding: 8 },
  item: { padding: 15, borderBottomWidth: 1, borderColor: '#eee' }
});