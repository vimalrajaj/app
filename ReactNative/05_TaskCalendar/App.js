import React, { useState } from 'react';
import { View, Text, TextInput, Button, FlatList, StyleSheet } from 'react-native';

export default function App() {
  const [task, setTask] = useState('');
  const [date, setDate] = useState('');
  const [tasks, setTasks] = useState([]);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Daily Task Calendar</Text>
      <TextInput placeholder="Date (e.g. 12 Oct)" onChangeText={setDate} style={styles.input} />
      <TextInput placeholder="Task Description" onChangeText={setTask} style={styles.input} />
      <Button title="Add to Calendar" onPress={() => setTasks([{date, task, id: Date.now().toString()}, ...tasks])} />
      <FlatList data={tasks} keyExtractor={item => item.id} renderItem={({item}) => (
        <View style={styles.item}><Text>{item.date}: {item.task}</Text></View>
      )} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 50, flex: 1 },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 20 },
  input: { borderBottomWidth: 1, marginBottom: 15, padding: 8 },
  item: { padding: 10, borderBottomWidth: 1, borderColor: '#eee' }
});